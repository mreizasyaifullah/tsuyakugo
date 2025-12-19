# Load Dependencies
import config
import speech_recognition as sr
import pygame
import time
from gtts import gTTS
import os
from mistralai import Mistral

# Set Mistral AI API Key
api_key = config.api_key
model = "open-mistral-nemo"

# Function to call Mistral AI for interpretation
def ask_mistral(prompt, language_A, language_B):
    client = Mistral(api_key=api_key)
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {"role": "system", "content": f"You are an interpreter. Your job is to accurately translate and interpret text between {language_map[language_A][0]} and {language_map[language_B][0]}. Maintain the meaning, tone, and context of the original message. Interpret concisely and do not speak too much."},
            {"role": "user", "content": prompt}]
    )
    return chat_response.choices[0].message.content

# Speech to Text
def speech_to_text(language):
    recognizer = sr.Recognizer()
    loop_status = True
    while(loop_status):
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout = 5, phrase_time_limit = 10)
        try:
            text = recognizer.recognize_google(audio, language = language)
            print(f"You said: {text}")
            loop_status = False
        except sr.UnknownValueError:
            print("I could not understand the audio")
            continue
        except sr.RequestError:
            print("Request failed")
            continue
    return text
    
# Text to Speech
def text_to_speech(text, language):
    # Initialize pygame mixer
    pygame.mixer.init()
    # Delete the file if it already exists
    if os.path.exists("speech.mp3"):
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        os.remove("speech.mp3")

    # Convert text to speech and save the file
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("speech.mp3")

    # Initialize pygame mixer
    pygame.mixer.init()

    # Wait a moment to ensure file writing is complete
    time.sleep(0.5)

    # Load and play the audio file
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()

    # Prevent script from exiting immediately
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

# Language List
language_map = {
    "A": ("Japanese", "ja"),
    "B": ("English", "en"),
    "C": ("Indonesian", "id"),
    "D": ("Chinese", "zh"),
    "E": ("Spanish", "es"),
    "F": ("Italian", "it"),
}

# Main function of TSUYAKUGO!
def run_tsuyakugo():
    # Program initialization - Greetings
    greetings_text = "Welcome to TSUYAKUGO! This is a speech-based chatbot designed to help you communicate with people in various language. We provide interpretation between you and your customer."
    greetings_text_jp = "「通訳合」へようこそ！これは、さまざまな言語で人々とのコミュニケーションを支援するために設計された音声ベースのチャットボットです。私たちはあなたとあなたの顧客の間の通訳を提供します。"
    print(greetings_text + "\n" + greetings_text_jp)
    text_to_speech("Welcome to TsuyakuGo!", "en")
    text_to_speech("TsuyakuGo!へようこそ！", "ja")

    language_A = 'default'
    while(not any(language_A in i for i in language_map.keys())):
        language_A = input("Please select Person A's language:\nA. Japanese\nB. English\nC. Indonesian\nD. Chinese\nE. Spanish\nF. Italian\nEnter only the first letter of your choice: ")
        if not any(language_A in i for i in language_map.keys()):
            print("Invalid input, please try again")
    language_B = 'default'
    while(not any(language_B in i for i in language_map.keys())):
        language_B = input("Please select Person B's language:\nA. Japanese\nB. English\nC. Indonesian\nD. Chinese\nE. Spanish\nF. Italian\nEnter only the first letter of your choice: ")
        if not any(language_B in i for i in language_map.keys()):
            print("Invalid input, please try again")
    
    while True:
        # Person A speaks
        print("Person A, please speak:")
        person_A_text = speech_to_text(language_map[language_A][1])
        if person_A_text is None:
            continue

        # Translate Person A's input to Person B's language
        prompt = f"Please translate the following from {language_A} to {language_B}: {person_A_text}"
        person_A_text_interpreted = ask_mistral(prompt, language_A, language_B)
        
        # Display and Play Person A's Interpreted Text
        print(f"Person B will hear: {person_A_text_interpreted}")
        text_to_speech(person_A_text_interpreted, language_map[language_B][1])

        print("Person B, please speak")
        person_B_text = speech_to_text(language_map[language_B][1])
        if person_B_text is None:
            continue
        
        # Translate Person B's input to Person A's language
        prompt = f"Please translate the following from {language_B} to {language_A}: {person_B_text}"
        person_B_text_interpreted = ask_mistral(prompt, language_A, language_B)

        # Display and Play Person B's Interpreted Text
        print(f"Person A will hear: {person_B_text_interpreted}")

        text_to_speech(person_B_text_interpreted, language_map[language_A][1])

# Run the program
run_tsuyakugo()       