from deep_translator import GoogleTranslator


class Translator:

    def __init__(self):
        pass

    def translate_text(self, text, source_language="auto", target_language="en"):
        """
        Translate text from source language to target language.

        Parameters:
        -----------
        text : str
            Text to translate

        source_language : str
            Language code (e.g. en, hi, fr)
            Default = auto

        target_language : str
            Language code

        Returns:
        --------
        dict
        """

        try:
            translated = GoogleTranslator(
                source=source_language,
                target=target_language
            ).translate(text)

            return {
                "success": True,
                "original_text": text,
                "translated_text": translated,
                "source_language": source_language,
                "target_language": target_language
            }

        except Exception as e:

            return {
                "success": False,
                "error": str(e)
            }


if __name__ == "__main__":

    translator = Translator()

    text = input("Enter text : ")

    source = input("Source language code (auto/en/hi/fr): ")

    target = input("Target language code : ")

    result = translator.translate_text(
        text=text,
        source_language=source,
        target_language=target
    )

    if result["success"]:

        print("\nOriginal Text:")
        print(result["original_text"])

        print("\nTranslated Text:")
        print(result["translated_text"])

    else:
        print(result["error"])