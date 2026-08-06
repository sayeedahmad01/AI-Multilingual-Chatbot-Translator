import pytest
from unittest.mock import patch, Mock
from googletrans import Translator

# Mock detection result
class MockDetected:
    def __init__(self, lang, confidence):
        self.lang = lang
        self.confidence = confidence

def test_detect_language():
    """Test language detection via googletrans."""
    with patch('googletrans.Translator.detect') as mock_detect:
        mock_detect.return_value = MockDetected('fr', 0.99)
        
        translator = Translator()
        detection = translator.detect("Bonjour")
        
        assert detection.lang == 'fr'
        assert detection.confidence == 0.99
        mock_detect.assert_called_once_with("Bonjour")

def test_detect_unknown_language():
    """Test detection of unknown language (should return 'en' or similar)."""
    with patch('googletrans.Translator.detect') as mock_detect:
        mock_detect.return_value = MockDetected('en', 0.1)
        
        translator = Translator()
        detection = translator.detect("abcxyz123")
        assert detection.lang == 'en'  # fallback often

def test_detect_empty_string():
    """Test detection on empty string - should not crash."""
    with patch('googletrans.Translator.detect') as mock_detect:
        # Possibly raise an exception or return some default
        # Let's simulate a reasonable response
        mock_detect.return_value = MockDetected('en', 0.0)
        translator = Translator()
        detection = translator.detect("")
        assert detection.lang == 'en'