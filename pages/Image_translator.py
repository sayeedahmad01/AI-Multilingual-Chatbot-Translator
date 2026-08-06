import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
from utils import get_languages, save_history

st.title("🖼️ Image Translator")

langs = st.session_state.get("languages", get_languages())
lang_codes = {v: k for k, v in langs.items()}

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source language", options=list(langs.values()), index=0, key="img_src")
with col2:
    tgt_lang = st.selectbox("Target language", options=list(langs.values()), index=1, key="img_tgt")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Extract & Translate"):
        try:
            # OCR
            src_code = lang_codes.get(src_lang, 'en')
            extracted = pytesseract.image_to_string(image, lang=src_code)
            if not extracted.strip():
                st.warning("No text found in image.")
            else:
                st.subheader("Extracted Text")
                st.text(extracted)

                # Translate
                translator = Translator()
                tgt_code = lang_codes.get(tgt_lang, 'es')
                result = translator.translate(extracted, src=src_code, dest=tgt_code)
                st.subheader("Translated Text")
                st.success(result.text)

                save_history({
                    "type": "Image",
                    "source": extracted[:100] + "...",  # preview
                    "translation": result.text,
                    "src_lang": src_lang,
                    "tgt_lang": tgt_lang
                })
        except Exception as e:
            st.error(f"Error: {e}")