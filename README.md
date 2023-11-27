# Speech-to-Text Converter with Translation and Calligraphy
A simple speech-to-text converter application built using Python and Tkinter, with additional features for text translation and calligraphy generation.

## Features
- **Speech-to-Text Conversion:** Record spoken language and convert it into written text.
- **Translation:** Translate the converted text into different languages using Google Translate.
- **Calligraphy Generation:** Apply various calligraphy styles to the converted or translated text.

## Requirements
Make sure you have the following dependencies installed:
- Python 3.x
- tkinter
- speech_recognition
- googletrans==4.0.0-rc1  # Ensure this version for compatibility
- ttkthemes  # If using custom themes for ttk widgets

You can install the required dependencies using the following command:
```bash
pip install -r requirements.txt

## Usage
Run the application by executing the speech_to_text_converter.py file.
Click the "Speak" button to record speech and convert it to text.
Select a target language from the dropdown and click "Translate" to translate the text.
Choose a calligraphy style from the dropdown and click "Calligraphy" to apply the style to the text.
The word count is displayed below the text area.

## Supported Languages
The application supports the following languages for speech recognition:

English (United States)
Hindi
Marathi
Tamil
Telugu
Korean
French
German
Japanese

## Contributing
If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. Contributions are welcome!

Feel free to customize this README file to better fit your project's specifics. Additionally, you may want to include a license file (`LICENSE`) in your repository and create a `requirements.txt` file with the dependencies if you don't have one already.




