STT — Speak It, Translate It, Letter It

A web-based speech-to-text application that converts spoken words into text, supports translation, and provides calligraphy-style text formatting.

Features

🎤 Speech-to-text conversion

🌐 Text translation

✍️ Calligraphy-style text formatting

📱 Responsive, mobile-friendly interface

🔄 Automatic speech recognition restart

📝 Handles long transcripts using text chunking

⚠️ Clear microphone and recognition error messages

Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Python, Flask

Speech Recognition: Web Speech API

Translation: Python translation service

Styling: Custom CSS

Project Structure

STT_FINAL/
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md

Installation

1. Clone the repository

git clone <your-repository-url>
cd STT_FINAL

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

4. Open in a browser

Open:

http://127.0.0.1:5000

For speech recognition, use Google Chrome or Microsoft Edge.

Speech Recognition

The application uses browser-based speech recognition.

Some browsers may automatically stop speech recognition after a short period of silence. The application detects an unexpected recognition stop and automatically attempts to restart the session while listening is still intended.

Microphone permission or hardware-related problems are handled separately and are reported to the user.

Translation

Long speech transcripts are divided into smaller, sentence-based chunks before translation.

This helps prevent long text from being skipped or incompletely processed by the translation service.

Browser Compatibility

Browser

Speech Recognition

Google Chrome

✅ Supported

Microsoft Edge

✅ Supported

Firefox

⚠️ Limited/Not supported

Safari

⚠️ Limited/Not supported

Notes

Allow microphone access when prompted by the browser.

An active internet connection may be required for speech recognition and translation.

Make sure your system has a working microphone.

License

This project is intended for educational and development purposes.