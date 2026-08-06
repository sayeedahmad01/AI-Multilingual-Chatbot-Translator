from datetime import datetime
from googletrans import LANGUAGES
import os
import pandas as pd

HISTORY_FILE = "data/history.csv"


# -----------------------------
# General Helper Functions
# -----------------------------
def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def is_empty(text):
    return len(text.strip()) == 0


def success(message):
    return {
        "success": True,
        "message": message
    }


def error(message):
    return {
        "success": False,
        "message": message
    }


# -----------------------------
# Language Functions
# -----------------------------
def get_languages():
    """
    Returns a dictionary like:
    {
        "English": "en",
        "Hindi": "hi",
        "French": "fr"
    }
    """
    return {name.title(): code for code, name in LANGUAGES.items()}


# -----------------------------
# History Functions
# -----------------------------
def save_history(input_text, translated_text, source_lang, target_lang):
    os.makedirs("data", exist_ok=True)

    row = {
        "Input Text": input_text,
        "Translated Text": translated_text,
        "Source Language": source_lang,
        "Target Language": target_lang,
        "Time": get_current_time()
    }

    if os.path.exists(HISTORY_FILE):
        df = pd.read_csv(HISTORY_FILE)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(HISTORY_FILE, index=False)


def load_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE)

    return pd.DataFrame(
        columns=[
            "Input Text",
            "Translated Text",
            "Source Language",
            "Target Language",
            "Time"
        ]
    )


def clear_history():
    if os.path.exists(HISTORY_FILE):
        os.remove(HISTORY_FILE)