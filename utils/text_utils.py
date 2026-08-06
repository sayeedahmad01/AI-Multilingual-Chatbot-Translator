import re


class TextUtils:

    @staticmethod
    def clean_text(text):

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    @staticmethod
    def word_count(text):

        return len(text.split())

    @staticmethod
    def character_count(text):

        return len(text)

    @staticmethod
    def sentence_count(text):

        return len(re.split(r"[.!?]+", text)) - 1

    @staticmethod
    def remove_extra_spaces(text):

        return " ".join(text.split())

    @staticmethod
    def to_lower(text):

        return text.lower()

    @staticmethod
    def to_upper(text):

        return text.upper()