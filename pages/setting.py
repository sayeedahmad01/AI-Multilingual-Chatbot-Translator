import streamlit as st
from utils import get_languages

st.title("⚙️ Settings")

# Language selection (customizable)
langs = get_languages()
selected_langs = st.multiselect(
    "Select languages to show in dropdowns (or keep all)",
    options=list(langs.values()),
    default=list(langs.values())
)
if st.button("Save Language Selection"):
    st.session_state.languages = {k: v for k, v in langs.items() if v in selected_langs}
    st.success("Language list updated!")

# Other settings
st.subheader("Appearance")
theme = st.selectbox("Theme", ["Light", "Dark"])
if theme == "Dark":
    st._config.set_option("theme.base", "dark")
    st._config.set_option("theme.primaryColor", "#FF4B4B")
else:
    st._config.set_option("theme.base", "light")
    st._config.set_option("theme.primaryColor", "#FF4B4B")

st.subheader("History")
keep_history = st.checkbox("Enable history storage", value=True)
st.session_state.keep_history = keep_history
if not keep_history:
    st.session_state.history = []

st.subheader("About")
st.info("This app uses googletrans (unofficial), gTTS, speech_recognition, and pytesseract.")