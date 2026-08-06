import streamlit as st
from gtts import gTTS
import io
import base64
from utils import get_languages

st.title("🔊 Text‑to‑Speech")

langs = st.session_state.get("languages", get_languages())
lang_codes = {v: k for k, v in langs.items()}

text = st.text_area("Enter text to speak", height=150)
lang = st.selectbox("Language", options=list(langs.values()), index=0)

if st.button("Generate Speech", type="primary"):
    if text.strip():
        try:
            code = lang_codes.get(lang, 'en')
            tts = gTTS(text, lang=code)
            audio_bytes = io.BytesIO()
            tts.write_to_fp(audio_bytes)
            audio_bytes.seek(0)
            audio_base64 = base64.b64encode(audio_bytes.read()).decode()
            audio_tag = f'<audio controls autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
            st.markdown(audio_tag, unsafe_allow_html=True)
            st.audio(audio_bytes, format="audio/mp3")  # fallback
        except Exception as e:
            st.error(f"TTS error: {e}")
    else:
        st.warning("Please enter text.")