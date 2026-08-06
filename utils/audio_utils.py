from pydub import AudioSegment


class AudioUtils:

    @staticmethod
    def mp3_to_wav(mp3_path, wav_path):

        audio = AudioSegment.from_mp3(mp3_path)

        audio.export(wav_path, format="wav")

    @staticmethod
    def wav_to_mp3(wav_path, mp3_path):

        audio = AudioSegment.from_wav(wav_path)

        audio.export(mp3_path, format="mp3")

    @staticmethod
    def get_audio_duration(audio_path):

        audio = AudioSegment.from_file(audio_path)

        return round(audio.duration_seconds, 2)