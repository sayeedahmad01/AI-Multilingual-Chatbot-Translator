import streamlit as st
from googletrans import Translator
from utils import get_languages, save_history
import PyPDF2
import docx
import io

st.title("📄 Document Translator")

langs = st.session_state.get("languages", get_languages())
lang_codes = {v: k for k, v in langs.items()}

uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])

col1, col2 = st.columns(2)
with col1:
    src_lang = st.selectbox("Source language", options=list(langs.values()), index=0, key="doc_src")
with col2:
    tgt_lang = st.selectbox("Target language", options=list(langs.values()), index=1, key="doc_tgt")

def extract_text(file):
    ext = file.name.split('.')[-1].lower()
    if ext == "txt":
        return file.read().decode("utf-8")
    elif ext == "pdf":
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif ext == "docx":
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    if not text.strip():
        st.warning("No extractable text found.")
    else:
        st.subheader("Extracted Text Preview")
        st.text(text[:1000] + ("..." if len(text)>1000 else ""))

        if st.button("Translate Document"):
            try:
                src_code = lang_codes.get(src_lang, 'en')
                tgt_code = lang_codes.get(tgt_lang, 'es')
                translator = Translator()
                # For large documents, we split into chunks (simple approach)
                chunk_size = 1000
                chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
                translated_chunks = []
                for chunk in chunks:
                    if chunk.strip():
                        result = translator.translate(chunk, src=src_code, dest=tgt_code)
                        translated_chunks.append(result.text)
                full_translation = "".join(translated_chunks)
                st.subheader("Translated Document")
                st.text_area("Translation", value=full_translation, height=300)

                save_history({
                    "type": "Document",
                    "source": text[:100] + "...",
                    "translation": full_translation[:100] + "...",
                    "src_lang": src_lang,
                    "tgt_lang": tgt_lang
                })

                # Option to download
                st.download_button("Download translation as .txt", data=full_translation, file_name="translated.txt")
            except Exception as e:
                st.error(f"Translation error: {e}")