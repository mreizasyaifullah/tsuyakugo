# Load Dependencies
import config
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
            {"role": "system", "content": f"You are an interpreter. Your job is to accurately translate and interpret text between {language_map[language_A][0]} and {language_map[language_B][0]}. Maintain the meaning, tone, and context of the original message."},
            {"role": "user", "content": prompt}]
    )
    return chat_response.choices[0].message.content

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
    greetings_text = "Welcome to TSUYAKUGO! This is a text-based chatbot designed to help you communicate with people in various language. We provide interpretation between you and your customer."
    greetings_text_jp = "「通訳合」へようこそ！これは、さまざまな言語で人々とコミュニケーションをとるのに役立つように設計されたテキストベースのチャットボットです。私たちはあなたとあなたの顧客の間の通訳を提供します"
    print(greetings_text + "\n" + greetings_text_jp)
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
        # Person A inputs text
        person_A_text = input(f"Person A ({language_map[language_A][0]}), enter your texts. Type 'stop' to end program: ")
        if not person_A_text.strip():
            continue
        if person_A_text == 'stop':
            break

        # Translate Person A's input to Person B's language
        prompt = f"Please interpret the following from {language_A} to {language_B}: {person_A_text}"
        person_A_text_interpreted = ask_mistral(prompt, language_A, language_B)

        print(f"Interpretation for Person B ({language_map[language_B][0]}): {person_A_text_interpreted}")

        # Person B inputs text
        person_B_text = input(f"Person B ({language_map[language_B][0]}), enter your texts. Type 'stop' to end program: ")
        if not person_B_text.strip():
            continue

        if person_B_text == 'stop':
            break

        # Translate Person B's input to Person A's language
        prompt = f"Please interpret the following from {language_B} to {language_A}: {person_B_text}"
        person_B_text_interpreted = ask_mistral(prompt, language_A, language_B)

        print(f"Interpretation for Person A ({language_map[language_A][0]}): {person_B_text_interpreted}")


# Run the program
run_tsuyakugo()