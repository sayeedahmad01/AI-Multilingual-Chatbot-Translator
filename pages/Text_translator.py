import streamlit as st
from googletrans import Translator
from utils.helper import get_languages, save_history

st.title("📝 Text Translator")

# Load language list from settings or use default
langs = st.session_state.get("languages", get_languages())

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source language", options=list(langs.values()), index=0)
with col2:
    tgt_lang = st.selectbox("Target language", options=list(langs.values()), index=1)

text = st.text_area("Enter text to translate", height=150)

if st.button("Translate", type="primary"):
    if text.strip():
        translator = Translator()
        # Map display name to code
        lang_codes = {v: k for k, v in langs.items()}
        src_code = lang_codes.get(src_lang, 'en')
        tgt_code = lang_codes.get(tgt_lang, 'es')
        try:
            result = translator.translate(text, src=src_code, dest=tgt_code)
            st.success(f"**Translation:** {result.text}")
            # Save to history
            save_history({
                "type": "Text",
                "source": text,
                "translation": result.text,
                "src_lang": src_lang,
                "tgt_lang": tgt_lang
            })
        except Exception as e:
            st.error(f"Translation error: {e}")
    else:
        st.warning("Please enter some text.")