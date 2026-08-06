from setuptools import setup, find_packages

setup(
    name="AI_Multilingual_Translator",
    version="1.0.0",
    author="Sayeed Ahmad",
    description="AI-powered multilingual translation application",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "deep-translator",
        "SpeechRecognition",
        "gtts",
        "langdetect",
        "easyocr",
        "opencv-python",
        "python-docx",
        "PyPDF2",
        "pandas",
        "numpy"
    ],
)