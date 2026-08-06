from langdetect import detect, detect_langs

# Language code to language name mapping
LANGUAGE_NAMES = {
    "af": "Afrikaans",
    "ar": "Arabic",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "ca": "Catalan",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "es": "Spanish",
    "et": "Estonian",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "hu": "Hungarian",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "kn": "Kannada",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mr": "Marathi",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pa": "Punjabi",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "sk": "Slovak",
    "sl": "Slovenian",
    "so": "Somali",
    "sq": "Albanian",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "th": "Thai",
    "tl": "Tagalog",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "vi": "Vietnamese",
    "zh-cn": "Chinese",
    "zh-tw": "Chinese (Traditional)"
}


def detect_language(text):
    """
    Detect the language code and language name.
    """
    try:
        code = detect(text)
        name = LANGUAGE_NAMES.get(code, code)
        return code, name
    except Exception:
        return None, None


def detect_language_with_confidence(text):
    """
    Detect language with confidence score.
    """
    try:
        result = detect_langs(text)[0]
        code = result.lang
        confidence = round(result.prob * 100, 2)
        name = LANGUAGE_NAMES.get(code, code)

        return {
            "language_code": code,
            "language_name": name,
            "confidence": confidence
        }

    except Exception:
        return None


if __name__ == "__main__":
    text = input("Enter text: ")

    code, name = detect_language(text)

    print("Language Code :", code)
    print("Language Name :", name)

    details = detect_language_with_confidence(text)

    print(details) 