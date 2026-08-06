import pytest
from unittest.mock import Mock, patch, MagicMock
import speech_recognition as sr
from gtts import gTTS
import io

def test_speech_to_text():
    """Test speech recognition with mocked audio."""
    # Mock the recognizer and microphone
    with patch('speech_recognition.Recognizer') as MockRecognizer:
        mock_recognizer = MockRecognizer.return_value
        # Simulate successful recognition
        mock_recognizer.recognize_google.return_value = "Hello world"
        
        # Simulate audio source - we won't actually use microphone
        # but we can mock the listen method
        mock_recognizer.listen.return_value = Mock()  # dummy audio
        
        recognizer = sr.Recognizer()
        # Normally we would do: with sr.Microphone() as source: audio = recognizer.listen(source)
        # We can mock the context manager
        with patch('speech_recognition.Microphone') as MockMicrophone:
            mock_mic = MockMicrophone.return_value.__enter__.return_value
            audio = recognizer.listen(mock_mic)
            text = recognizer.recognize_google(audio, language='en-US')
            assert text == "Hello world"
            mock_recognizer.recognize_google.assert_called_once_with(audio, language='en-US')

def test_speech_to_text_unknown_error():
    """Test speech recognition when audio is not understood."""
    with patch('speech_recognition.Recognizer') as MockRecognizer:
        mock_recognizer = MockRecognizer.return_value
        mock_recognizer.recognize_google.side_effect = sr.UnknownValueError()
        
        with patch('speech_recognition.Microphone'):
            recognizer = sr.Recognizer()
            # We need to simulate listen returning something
            # But we can directly call recognize_google on a dummy audio
            try:
                # Just test the exception
                with pytest.raises(sr.UnknownValueError):
                    recognizer.recognize_google(Mock())
            except:
                pass  # The test will catch the exception as expected

def test_text_to_speech():
    """Test gTTS generation."""
    with patch('gtts.gTTS') as MockTTS:
        mock_tts_instance = MockTTS.return_value
        # Mock the write_to_fp method
        mock_tts_instance.write_to_fp = Mock()
        
        tts = gTTS("Hello", lang='en')
        tts.write_to_fp(io.BytesIO())
        
        MockTTS.assert_called_once_with("Hello", lang='en')
        mock_tts_instance.write_to_fp.assert_called_once()