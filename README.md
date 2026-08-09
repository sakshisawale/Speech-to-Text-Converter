# STT — Speak It, Translate It, Letter It

A web-based speech-to-text application that converts spoken words into text, supports translation, and provides calligraphy-style text formatting.

## Features
- 🎤 Speech-to-text conversion
- 🌐 Text translation
- ✍️ Calligraphy-style text formatting
- 📱 Responsive, mobile-friendly interface
- 🔄 Automatic speech recognition restart
- 📝 Handles long transcripts using text chunking
- ⚠️ Clear microphone and recognition error messages

## Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Speech Recognition:** Web Speech API
- **Translation:** Python translation service
- **Styling:** Custom CSS

## Project Structure
```
STT_FINAL/
├── static/
│   ├── css/style.css
│   └── js/script.js
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Installation
```bash
git clone <your-repository-url>
cd STT_FINAL
pip install -r requirements.txt
python app.py
```
The application can be tested locally before deployment.

## Deployment
This project is designed to be deployed as a Flask web application on a cloud hosting platform.

**Live Demo:** <your-deployed-application-url>

Deployment requirements:
- Python runtime
- Dependencies from `requirements.txt`
- Flask application entry point
- A production web server such as Gunicorn
- Required environment variables, if applicable

Typical production start command:
```
gunicorn app:app
```
Exact configuration may vary depending on the hosting platform.

## Speech Recognition
Uses the browser's Web Speech API. Some browsers stop recognition after a short silence — the app detects this and automatically restarts the session while listening is still intended. Microphone/hardware issues are reported separately to the user.

## Translation
Long transcripts are split into sentence-based chunks before translation to prevent text from being skipped or incompletely processed.

## Browser Compatibility
| Browser | Speech Recognition |
|---|---|
| Google Chrome | ✅ Supported |
| Microsoft Edge | ✅ Supported |
| Firefox | ⚠️ Limited/Not supported |
| Safari | ⚠️ Limited/Not supported |

## Notes
- Allow microphone access when prompted.
- Speech recognition may require an internet connection.
- Browser microphone permissions must be enabled for the deployed site.
- Do not commit passwords, API keys, tokens, or other sensitive configuration to the repository.

## License
This project is intended for educational and development purposes.