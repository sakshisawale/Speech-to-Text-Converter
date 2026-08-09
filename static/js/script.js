const micBtn = document.getElementById("micBtn");
const micStatus = document.getElementById("micStatus");
const speechLang = document.getElementById("speechLang");
const outputText = document.getElementById("outputText");
const interim = document.getElementById("interim");
const wordCount = document.getElementById("wordCount");
const translateBtn = document.getElementById("translateBtn");
const translateLang = document.getElementById("translateLang");
const calligraphyBtn = document.getElementById("calligraphyBtn");
const calligraphyStyle = document.getElementById("calligraphyStyle");
const clearBtn = document.getElementById("clearBtn");
const toast = document.getElementById("toast");

let recognition = null;
let shouldListen = false;   // user's intent (mic toggled on/off)
let isRunning = false;      // recognition engine's actual state
let restartAttempts = 0;
const MAX_RESTART_ATTEMPTS = 5;

function showToast(message) {
  toast.textContent = message;
  toast.classList.add("show");
  clearTimeout(showToast._t);
  showToast._t = setTimeout(() => toast.classList.remove("show"), 2800);
}

function updateWordCount() {
  const words = outputText.value.trim().split(/\s+/).filter(Boolean);
  wordCount.textContent = `${words.length} word${words.length === 1 ? "" : "s"}`;
}

function capitalizeSentences(text) {
  return text.replace(/(^\s*\w|[.!?]\s*\w)/g, (c) => c.toUpperCase());
}

const SpeechRecognitionAPI = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!window.isSecureContext) {
  micStatus.textContent = "Open this over http://localhost or https:// for the mic to work.";
  micBtn.disabled = true;
} else if (!SpeechRecognitionAPI) {
  micStatus.textContent = "Speech recognition isn't supported here — use Chrome or Edge.";
  micBtn.disabled = true;
} else {
  recognition = new SpeechRecognitionAPI();
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.maxAlternatives = 1;

  recognition.onstart = () => {
    isRunning = true;
    restartAttempts = 0;
    micBtn.classList.add("listening");
    micStatus.textContent = "Listening…";
  };

  recognition.onresult = (event) => {
    let finalChunk = "";
    let interimChunk = "";
    for (let i = event.resultIndex; i < event.results.length; i++) {
      const transcript = event.results[i][0].transcript;
      if (event.results[i].isFinal) {
        finalChunk += transcript;
      } else {
        interimChunk += transcript;
      }
    }
    if (finalChunk) {
      const current = outputText.value.trim();
      const next = (current + " " + capitalizeSentences(finalChunk.trim())).trim();
      outputText.value = next;
      updateWordCount();
    }
    interim.textContent = interimChunk;
  };

  recognition.onerror = (event) => {
    // "no-speech" and "aborted" happen naturally in continuous mode and
    // are not real failures — recovered by the auto-restart in onend.
    // Only surface the errors that actually need the user's attention.
    if (event.error === "not-allowed" || event.error === "service-not-allowed") {
      showToast("Microphone access is blocked — allow it in your browser's site settings.");
      shouldListen = false;
    } else if (event.error === "audio-capture") {
      showToast("No microphone was found. Check it's connected and not used by another app.");
      shouldListen = false;
    } else if (event.error === "network") {
      showToast("Network hiccup during recognition — retrying…");
    }
    // no-speech / aborted: stay silent, let onend handle recovery
  };

  recognition.onend = () => {
    isRunning = false;
    micBtn.classList.remove("listening");
    interim.textContent = "";

    if (shouldListen && restartAttempts < MAX_RESTART_ATTEMPTS) {
      // Chrome frequently ends a "continuous" session on its own after a
      // pause — restart automatically so it feels like uninterrupted
      // listening instead of surfacing an error to the user.
      restartAttempts += 1;
      micStatus.textContent = "Listening…";
      setTimeout(() => {
        if (shouldListen) {
          try {
            recognition.start();
          } catch (e) {
            /* already running — ignore */
          }
        }
      }, 250);
    } else {
      micStatus.textContent = "Tap to speak";
      if (restartAttempts >= MAX_RESTART_ATTEMPTS) {
        showToast("Recognition kept dropping — tap the mic to start fresh.");
      }
      restartAttempts = 0;
      shouldListen = false;
    }
  };
}

micBtn.addEventListener("click", () => {
  if (!recognition) return;

  if (shouldListen) {
    shouldListen = false;
    recognition.stop();
    return;
  }

  shouldListen = true;
  restartAttempts = 0;
  recognition.lang = speechLang.value;

  if (isRunning) return;
  try {
    recognition.start();
  } catch (e) {
    // start() throws if called while already starting — safe to ignore
  }
});

// --- Translate
translateBtn.addEventListener("click", async () => {
  const text = outputText.value.trim();
  if (!text) {
    showToast("Nothing to translate yet.");
    return;
  }
  translateBtn.disabled = true;
  translateBtn.textContent = "Translating…";
  try {
    const res = await fetch("/api/translate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, target: translateLang.value }),
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error);
    outputText.value = data.translated;
    updateWordCount();
  } catch (e) {
    showToast(e.message || "Translation failed.");
  } finally {
    translateBtn.disabled = false;
    translateBtn.textContent = "Translate";
  }
});

// --- Calligraphy
const calligraphyStyles = {
  Reverse: (t) => t.split("").reverse().join(""),
  UpperCase: (t) => t.toUpperCase(),
  LowerCase: (t) => t.toLowerCase(),
  DoubleSpace: (t) => t.split(/\s+/).join("  "),
  SwapCase: (t) =>
    t
      .split("")
      .map((c) => (c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()))
      .join(""),
  Cursive: (t) => {
    const normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const cursive = "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵";
    return t
      .split("")
      .map((c) => {
        const idx = normal.indexOf(c);
        return idx === -1 ? c : cursive[idx];
      })
      .join("");
  },
};

calligraphyBtn.addEventListener("click", () => {
  const text = outputText.value.trim();
  if (!text) {
    showToast("Nothing to style yet.");
    return;
  }
  const fn = calligraphyStyles[calligraphyStyle.value];
  if (fn) {
    outputText.value = fn(text);
    updateWordCount();
  }
});

// --- Clear
clearBtn.addEventListener("click", () => {
  outputText.value = "";
  interim.textContent = "";
  updateWordCount();
});

outputText.addEventListener("input", updateWordCount);
updateWordCount();
