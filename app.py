import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from deep_translator import GoogleTranslator

def main():
    st.title("Speech-to-Language Translation Tool")
    st.subheader("Convert speech to text and translate into different languages!")

    # Language options
    languages = {
        "French": "fr",
        "Spanish": "es",
        "German": "de",
        "Hindi": "hi",
        "Chinese (Simplified)": "zh-cn",
    }
    
    # Select target language
    target_language = st.selectbox("Select the target language:", list(languages.keys()))
    lang_code = languages[target_language]

    # Speech recognition
    recognizer = sr.Recognizer()

    st.write("Click the button below and start speaking:")
    if st.button("Record"):
        with sr.Microphone() as source:
            st.write("Listening...")
            try:
                audio_data = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                st.write("Processing...")
                text = recognizer.recognize_google(audio_data)
                st.write(f"Recognized Speech: {text}")

                # Translation


                # Translation
                translator = GoogleTranslator(source='auto', target=lang_code)
                translated_text = translator.translate(text)
                st.write(f"Translated Text ({target_language}): {translated_text}")

            except sr.UnknownValueError:
                st.error("Sorry, could not understand the audio.")
            except sr.RequestError:
                st.error("API error. Please check your internet connection.")
if __name__ == "__main__":
    main()