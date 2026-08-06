# 🌍 AI Multilingual Chatbot & Translator

> An AI-powered multilingual assistant built with Python and Streamlit for intelligent conversations, language translation, voice processing, OCR-based image translation, and document translation.

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-black?logo=openai)](https://openai.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/sayeedahmad01/AI-Multilingual-Chatbot-Translator)

---

## 📌 Overview

**AI Multilingual Chatbot & Translator** is a Streamlit-based AI application designed to make communication across languages easier.

The application combines **Generative AI, Natural Language Processing, speech processing, OCR, and translation technologies** into a single user-friendly interface.

Users can interact with an AI chatbot, translate text between languages, process speech, translate images and documents, and maintain translation history.

---

## ✨ Key Features

### 🤖 AI Chatbot
- Intelligent conversational AI
- Context-aware chat history
- General question answering
- Technical assistance
- Friendly and concise responses

### 🌐 Multilingual Translation
- Text-to-text translation
- Multiple language support
- Automatic language detection
- Context-aware translation

### 🎙️ Speech Processing
- Voice-to-text conversion
- Text-to-speech generation
- Voice-to-voice translation workflow

### 🖼️ Image Translation
- Upload images containing text
- Extract text using OCR
- Translate extracted text into the selected language

### 📄 Document Translation
- Process supported document files
- Extract text
- Translate document content

### 🕘 Translation History
- Store previous conversations
- Maintain translation history during the session
- Clear chat history when required

### 🔐 Secure API Configuration
- API credentials are loaded through Streamlit secrets
- Sensitive credentials are excluded from GitHub
- `.gitignore` is used to prevent accidental secret commits

---

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| AI / LLM | OpenAI API |
| NLP | Natural Language Processing |
| OCR | OCR-based text extraction |
| Speech | Speech Recognition / Text-to-Speech |
| Data Processing | Pandas, NumPy |
| Version Control | Git & GitHub |
| Environment | Python Virtual Environment |

---

## 🏗️ Project Architecture

```text
User
  │
  ▼
Streamlit Web Interface
  │
  ├── AI Chatbot
  │      └── OpenAI API
  │
  ├── Text Translation
  │      └── Language Processing
  │
  ├── Voice Processing
  │      ├── Speech-to-Text
  │      └── Text-to-Speech
  │
  ├── Image Translation
  │      └── OCR → Translation
  │
  ├── Document Translation
  │      └── Text Extraction → Translation
  │
  └── Translation History
