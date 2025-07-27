import os
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

engine = pyttsx3.init()

template = """
Answer the question below based on the provided context.

Context:
{context}

Question:
{question}

Answer:
"""
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

CHAT_HISTORY_FILE = "chat_history.txt"

if os.path.exists(CHAT_HISTORY_FILE):
    with open(CHAT_HISTORY_FILE, "r") as file:
        chat_history = file.read()
else:
    chat_history = ""

def speak(text):
    """Text-to-speech function."""
    engine.say(text)
    engine.runAndWait()

def chat_with_ollama(query, context=""):
    """Interact with the Ollama model."""
    try:
        result = chain.invoke({"context": context, "question": query})
        return result
    except Exception as e:
        return f"Error: {e}"

def take_voice_command():
    """Capture voice input and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        try:
            audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            speak("Sorry, I didn't catch that. Please try again.")
            return None

def save_chat_history():
    """Save the chat history to a file."""
    with open(CHAT_HISTORY_FILE, "w") as file:
        file.write(chat_history)

def handle_query(query):
    """Handle user queries and generate responses."""
    global chat_history

    if "open" in query.lower():

        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.org",
            "google": "https://www.google.com"
        }
        for site_name, site_url in sites.items():
            if f"open {site_name}".lower() in query.lower():
                speak(f"Opening {site_name}...")
                webbrowser.open(site_url)
                return

    elif "the time" in query.lower():

        current_time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {current_time}.")
        return

    elif "quit" in query.lower():

        speak("Goodbye! Have a great day!")
        save_chat_history()
        exit()

    elif "reset chat" in query.lower():

        global chat_history
        chat_history = ""
        speak("Chat history has been reset.")
        save_chat_history()
        return

    else:

        response = chat_with_ollama(query, chat_history)
        chat_history += f"User: {query}\nBuddy: {response}\n"
        save_chat_history()
        speak(response)
        print(f"AI: {response}")

def main():
    """Main function to handle user interaction."""
    print("Welcome to Buddy AI!")
    speak("Welcome to Buddy AI! Do you want to use voice or text?")
    mode = input("Enter 'voice' or 'text': ").strip().lower()

    while True:
        if mode == "voice":
            query = take_voice_command()
            if not query:
                continue
        elif mode == "text":
            query = input("Type your query: ").strip()
        else:
            speak("Invalid mode. Please restart and choose either voice or text.")
            break

        handle_query(query)

if __name__ == "__main__":
    main()

