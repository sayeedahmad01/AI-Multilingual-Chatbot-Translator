import pytest
from unittest.mock import Mock, patch
from googletrans import Translator

# Assuming we have a helper function in utils, but we'll test raw usage
from utils import get_languages  # if needed

# Mock translation result
class MockTranslated:
    def __init__(self, text, src, dest):
        self.text = text
        self.src = src
        self.dest = dest

def test_translate_text():
    """Test translation via googletrans with mocked translator."""
    with patch('googletrans.Translator.translate') as mock_translate:
        # Setup mock
        mock_translate.return_value = MockTranslated("Hola", "en", "es")
        
        translator = Translator()
        result = translator.translate("Hello", src='en', dest='es')
        
        assert result.text == "Hola"
        assert result.src == "en"
        assert result.dest == "es"
        mock_translate.assert_called_once_with("Hello", src='en', dest='es')

def test_translate_empty_text():
    """Test translation of empty string - should still work (returns empty)."""
    with patch('googletrans.Translator.translate') as mock_translate:
        mock_translate.return_value = MockTranslated("", "en", "es")
        translator = Translator()
        result = translator.translate("", src='en', dest='es')
        assert result.text == ""

def test_translate_auto_detect():
    """Test translation with source language auto-detection."""
    with patch('googletrans.Translator.translate') as mock_translate:
        mock_translate.return_value = MockTranslated("Bonjour", "fr", "en")
        translator = Translator()
        # Using src=None to auto-detect
        result = translator.translate("Bonjour", src=None, dest='en')
        assert result.text == "Bonjour"
        assert result.src == "fr"
        mock_translate.assert_called_once_with("Bonjour", src=None, dest='en')