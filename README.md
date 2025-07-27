# Tech-Pocket
TechPocket is a local AI assistant that runs LLaMA 3.2 using Ollama, enabling offline, private interactions with a powerful language model. It supports tasks like code help, document analysis, and Q&amp;A through a simple CLI or web interface, ensuring fast performance and full data privacy without cloud dependence. 

# 🤖 TechPocket – Offline Voice & Text AI Assistant with LLaMA 3.2 via Ollama

**TechPocket** is a simple yet powerful local AI assistant that uses **Meta’s LLaMA 3.2 model** through **Ollama**. It supports both **voice and text input** and allows users to interact with the AI entirely offline. The assistant can open websites, tell time, and answer general queries using local LLM inference.

---

## 📂 Project Structure

techpocket/
├── main.py # Main voice/text interface with Ollama integration
├── openaitest.py # Test script to verify Ollama model response

Edit

---

## 🧠 Features

- Run LLaMA 3.2 locally with Ollama (no cloud API required)
- Voice and text input options using `speech_recognition` and `pyttsx3`
- Persistent chat history storage in `chat_history.txt`
- Smart commands: open websites, check time, reset chat, and more
- Test script included to validate LLaMA 3.2 output

---

## ⚙️ Requirements

- Python 3.8+
- Ollama installed and LLaMA 3.2 model pulled



Edit
Or install manually:
pip install langchain speechrecognition pyttsx3

Edit

---

## 🚀 Getting Started

1. **Install Ollama**  
 Download and install from [https://ollama.com](https://ollama.com)

2. **Run the model**

 ollama run llama3
Run the main assistant



Edit
python main.py
Choose between voice or text interaction at runtime.

Test the Ollama setup


Edit
python openaitest.py
💬 Supported Commands
"Open YouTube/Google/Wikipedia" – Opens site in browser

"What is the time?" – Speaks current time

"Reset chat" – Clears chat history

"Quit" – Exits the assistant

Ask any general question (e.g., "What is quantum computing?")

📌 Notes
Ensure your microphone is working for voice mode.

All AI responses are generated locally via langchain_ollama.
