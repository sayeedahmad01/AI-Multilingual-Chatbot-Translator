import streamlit as st
import speech_recognition as sr
from utils import get_languages

st.title("🗣️ Speech‑to‑Text")

langs = st.session_state.get("languages", get_languages())
lang_codes = {v: k for k, v in langs.items()}

lang = st.selectbox("Language", options=list(langs.values()), index=0)

if st.button("🎙️ Start Recording"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            st.info("Recognizing...")
            code = lang_codes.get(lang, 'en')
            text = recognizer.recognize_google(audio, language=code)
            st.success(f"**Transcribed text:** {text}")
            # Optionally copy to clipboard (using st.text_input)
            st.text_input("Copy text", value=text)
        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Speech recognition error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")