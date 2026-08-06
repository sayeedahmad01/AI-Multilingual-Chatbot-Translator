import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import io
import base64
from utils import get_languages, save_history

st.title("🎤 Voice Translator")

langs = st.session_state.get("languages", get_languages())

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source language", options=list(langs.values()), index=0, key="voice_src")
with col2:
    tgt_lang = st.selectbox("Target language", options=list(langs.values()), index=1, key="voice_tgt")

# Speech recognition
if st.button("🎙️ Record and Translate"):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)
            st.info("Processing...")
            # Recognize speech using Google Web Speech API (free)
            lang_codes = {v: k for k, v in langs.items()}
            src_code = lang_codes.get(src_lang, 'en')
            text = recognizer.recognize_google(audio, language=src_code)
            st.write(f"**Recognized:** {text}")

            # Translate
            translator = Translator()
            tgt_code = lang_codes.get(tgt_lang, 'es')
            result = translator.translate(text, src=src_code, dest=tgt_code)
            st.success(f"**Translation:** {result.text}")

            # Save history
            save_history({
                "type": "Voice",
                "source": text,
                "translation": result.text,
                "src_lang": src_lang,
                "tgt_lang": tgt_lang
            })

            # Option to play TTS of translation
            if st.button("🔊 Play translation as speech"):
                tts = gTTS(result.text, lang=tgt_code)
                audio_bytes = io.BytesIO()
                tts.write_to_fp(audio_bytes)
                audio_bytes.seek(0)
                audio_base64 = base64.b64encode(audio_bytes.read()).decode()
                audio_tag = f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
                st.markdown(audio_tag, unsafe_allow_html=True)

        except sr.UnknownValueError:
            st.error("Could not understand audio")
        except sr.RequestError as e:
            st.error(f"Speech recognition service error: {e}")
        except Exception as e:
            st.error(f"Error: {e}")