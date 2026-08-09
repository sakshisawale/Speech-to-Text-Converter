# STT — speak it, translate it, letter it

A dark, mobile-style web app for speech-to-text, translation, and calligraphy styling.

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

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000 in Chrome or Edge.

## Deploy to Vercel
1. Push this project to a GitHub repository.
2. Go to vercel.com → New Project → import the repository.
3. Framework preset: Other. Vercel will detect `vercel.json` automatically.
4. Click Deploy.

No environment variables are required. The `vercel.json` and `api/index.py`
files route requests to the Flask app as a serverless function.

## Notes
- Speech recognition requires Chrome or Edge and mic permission.
- Deployed apps run over HTTPS, which the browser's speech API requires.

## License
All Rights Reserved.
