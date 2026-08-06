import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def microphone_to_text(self):
        """
        Convert microphone speech to text.
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                print("🎙️ Speak now...")
                audio = self.recognizer.listen(source)

            text = self.recognizer.recognize_google(audio)
            return {
                "success": True,
                "text": text
            }

        except sr.UnknownValueError:
            return {
                "success": False,
                "error": "Could not understand the audio."
            }

        except sr.RequestError:
            return {
                "success": False,
                "error": "Speech Recognition service is unavailable."
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }

    def audio_file_to_text(self, audio_path):
        """
        Convert an audio file (.wav) to text.
        """
        try:
            with sr.AudioFile(audio_path) as source:
                audio = self.recognizer.record(source)

            text = self.recognizer.recognize_google(audio)

            return {
                "success": True,
                "text": text
            }

        except sr.UnknownValueError:
            return {
                "success": False,
                "error": "Could not understand the audio."
            }

        except sr.RequestError:
            return {
                "success": False,
                "error": "Speech Recognition service unavailable."
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


if __name__ == "__main__":
    stt = SpeechToText()

    print("1. Microphone")
    print("2. Audio File")

    choice = input("Choose (1/2): ")

    if choice == "1":
        result = stt.microphone_to_text()

    else:
        path = input("Enter audio file path (.wav): ")
        result = stt.audio_file_to_text(path)

    if result["success"]:
        print("\nRecognized Text:")
        print(result["text"])
    else:
        print("\nError:")
        print(result["error"])