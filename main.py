import tkinter as tk
from tkinter import scrolledtext, ttk
import speech_recognition as sr
from googletrans import Translator
from tkinter import messagebox

# Define supported languages
languages = ["English", "Hindi", "Marathi", "Tamil", "Telugu", "Korean", "French",  "Japanese"]

# Replace this placeholder with the actual calligraphy generator
# Replace this with your actual calligraphy generation logic
def generate_calligraphy(text, style):
    calligraphy_styles = {
        "Reverse": lambda t: t[::-1],
        "UpperCase": lambda t: t.upper(),
        "LowerCase": lambda t: t.lower(),
        "DoubleSpace": lambda t: "  ".join(t.split()),
        "SwapCase": lambda t: t.swapcase()
        # Add more calligraphy styles as needed
    }

    if style in calligraphy_styles:
        return calligraphy_styles[style](text)
    else:
        messagebox.showinfo("Error", "Invalid calligraphy style selected.")
        return None
        
def calculate_word_count(text):
    words = text.split()
    return len(words)

def record_audio(language='en-US'):  # Default to English (United States)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Say something in {language}:")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language)
        current_text = output_text.get("1.0", tk.END)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, current_text + text)
        output_text.config(state=tk.DISABLED)
        update_word_count(current_text + text)
    except sr.UnknownValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Could not understand audio in {language}")
        output_text.config(state=tk.DISABLED)
    except sr.RequestError as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        output_text.config(state=tk.DISABLED)

def translate_text():
    selected_language = language_combobox.get()
    if not selected_language or selected_language == "Select Language":
        messagebox.showinfo("Error", "Please select a language before translating.")
    else:
        translator = Translator()
        input_text = output_text.get("1.0", tk.END)
        translated_text = translator.translate(input_text, dest=selected_language).text
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, translated_text)
        output_text.config(state=tk.DISABLED)
        update_word_count(translated_text)

def generate_calligraphy_text():
    input_text = output_text.get("1.0", tk.END)
    selected_style = calligraphy_style_combobox.get()

    if not selected_style or selected_style == "Select Style":
        messagebox.showinfo("Error", "Please select a calligraphy style.")
    else:
        # Replace this with your actual calligraphy generation logic
        calligraphy_text = generate_calligraphy(input_text, selected_style)

        if calligraphy_text is not None:
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, calligraphy_text)
            output_text.config(state=tk.DISABLED)
            update_word_count(calligraphy_text)
        else:
            output_text.config(state=tk.NORMAL)
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, "Error in calligraphy generation")
            output_text.config(state=tk.DISABLED)

def clear_text():
    output_text.config(state=tk.NORMAL)
    output_text.delete(1.0, tk.END)
    output_text.config(state=tk.DISABLED)
    word_count_label.config(text="Word Count: 0")

def update_word_count(text):
    word_count = calculate_word_count(text)
    word_count_label.config(text=f"Word Count: {word_count}")

# Create the main window
window = tk.Tk()
window.title("Speech to Text System")

# Create and configure the text widget for output
output_text = scrolledtext.ScrolledText(window, width=100, height=20)
output_text.config(state=tk.DISABLED)

# Create Record, Translate, Calligraphy, Clear, and Exit buttons
record_button = tk.Button(window, text="Speak", command=lambda: record_audio(language_combobox.get()), bd=5)
exit_button = tk.Button(window, text="Exit", command=window.destroy, bd=5)
clear_button = tk.Button(window, text="Clear", command=clear_text, bd=5)

language_combobox = ttk.Combobox(window, values=languages)
language_combobox.set("Select Language")
translate_button = tk.Button(window, text="Translate", command=translate_text, bd=5)
# Add calligraphy style combobox
calligraphy_styles = ["Select Style", "Reverse", "UpperCase", "LowerCase", "DoubleSpace", "SwapCase"]
calligraphy_style_combobox = ttk.Combobox(window, values=calligraphy_styles)
calligraphy_style_combobox.set("Select Style")

calligraphy_button = tk.Button(window, text="Calligraphy", command=generate_calligraphy_text, bd=5)
word_count_label = tk.Label(window, text="Word Count: 0")

# Pack widgets
output_text.pack(pady=10)
record_button.pack(side=tk.LEFT, padx=10)
exit_button.pack(side=tk.LEFT, padx=10)
clear_button.pack(side=tk.LEFT, padx=10)
language_combobox.pack(side=tk.LEFT, padx=5)
translate_button.pack(side=tk.LEFT, padx=5)
calligraphy_style_combobox.pack(side=tk.LEFT, padx=5)
calligraphy_button.pack(side=tk.LEFT, padx=5)
word_count_label.pack(pady=5)

# Run the Tkinter event loop
window.mainloop()
