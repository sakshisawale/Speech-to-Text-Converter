from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import re

app = Flask(__name__)

TRANSLATE_LANG_CODES = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Tamil": "ta",
    "Telugu": "te",
    "Korean": "ko",
    "French": "fr",
    "Japanese": "ja",
}

MAX_CHUNK_CHARS = 4000


def chunk_text(text, max_chars=MAX_CHUNK_CHARS):
    sentences = re.split(r'(?<=[.!?।])\s+', text.strip())
    chunks, current = [], ""
    for sentence in sentences:
        if len(current) + len(sentence) + 1 <= max_chars:
            current = f"{current} {sentence}".strip()
        else:
            if current:
                chunks.append(current)
            current = sentence
    if current:
        chunks.append(current)
    return chunks or [text]


@app.route("/")
def index():
    return render_template("index.html", languages=list(TRANSLATE_LANG_CODES.keys()))


@app.route("/api/translate", methods=["POST"])
def translate():
    data = request.get_json(force=True)
    text = (data.get("text") or "").strip()
    target_name = data.get("target", "English")

    if not text:
        return jsonify({"error": "No text provided."}), 400

    target_code = TRANSLATE_LANG_CODES.get(target_name, "en")

    try:
        chunks = chunk_text(text)
        translated_chunks = []
        for chunk in chunks:
            result = GoogleTranslator(source="auto", target=target_code).translate(chunk)
            translated_chunks.append(result if result else chunk)
        return jsonify({"translated": " ".join(translated_chunks)})
    except Exception as e:
        return jsonify({"error": f"Translation failed: {e}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
