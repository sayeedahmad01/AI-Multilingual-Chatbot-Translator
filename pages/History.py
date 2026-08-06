import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📜 Translation History")

if "history" not in st.session_state:
    st.session_state.history = []

history = st.session_state.history

if not history:
    st.info("No translations recorded yet.")
else:
    # Display in a table
    df = pd.DataFrame(history)
    # Add timestamp if not present (we can add a timestamp when saving)
    if "timestamp" not in df.columns:
        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.dataframe(df[["timestamp", "type", "src_lang", "tgt_lang", "source", "translation"]])

    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()