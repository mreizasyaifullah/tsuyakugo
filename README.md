<img width="178" height="94" alt="image" src="https://github.com/user-attachments/assets/4ff88403-99ce-44d2-89e2-a24be4522e12" />

## About TSUYAKUGO!

TSUYAKUGO! is an AI-based online interpreter prototype designed to facilitate real-time multilingual communication. The system serves as an intermediary between two individuals who speak different languages.  The name is derived from Japanese words 通訳 (tsuuyaku – interpretation) and 合 (gou – match/ together), which translates to “to match persons with different languages through interpreting” from writer’s perspective.

<img width="281" height="199" alt="image" src="https://github.com/user-attachments/assets/84f475d0-5c08-4bab-a346-51b009b58f3f" />

Figure 1. Example Use Case to Utilize TSUYAKUGO!

TSUYAKUGO! operates in a turn-based dialogue system, where each person speaks or types their message, and the AI interprets and delivers the translation in both text and speech format. By leveraging large language models (LLMs), speech recognition, and text-to-speech synthesis, the system tries to conduct natural and fluent conversation between the two interlocutors.

## Interpretation Modes

TSUYAKUGO! offers two modes of interpretation to accommodate different user preferences and environments:
1.	Speech-Based Interpretation
•	This mode allows users to speak their message into a microphone.
•	The system utilizes speech recognition (STT – Speech-to-Text) to convert spoken language into text.
•	The AI model processes the input, generates an accurate translation, and then converts it back into speech (TTS – Text-to-Speech) for the listener.

2.	Text-Based Interpretation
•	Users manually input text into the system.
•	The AI model interprets the message and provides a translated text output.
•	Suitable for chat-based communication, official documents, or messaging applications.

## How Does TSUYAKUGO! Work?

TSUYAKUGO! runs in sequential flow to facilitate real-time interpretation between two speakers. The process can be shown as follows:

<img width="371" height="230" alt="image" src="https://github.com/user-attachments/assets/b05a9bfd-0b3e-4c7a-8816-57e40a01e668" />

Figure 2. Speech-Based Interpretation Flow Diagram

<img width="305" height="224" alt="image" src="https://github.com/user-attachments/assets/c7d59d86-5724-430d-a490-c9f0dfab4b47" />

Figure 3. Text-Based Interpretation Flow Diagram

## Large Language Model

TSUYAKUGO! is powered by Mistral AI using its open-mistral-nemo model. This is a free large language model (LLM) optimized for multilingual tasks. Here are the features provided by Mistral AI through constructed prompt:
•	Multilingual Translation – Supports various languages with contextual awareness.
•	Context Preservation – Maintains the meaning, tone, and intent of the original message.
•	Task-Oriented Response – Designed specifically for interpretation rather than casual conversation.
Mistral AI functions by processing text input and generating contextually accurate translations using deep learning models. The model follows these steps:
1.	Tokenization: The input text is broken down into tokens (word fragments).
2.	Context Encoding: The model analyzes the context of the sentence.
3.	Translation Generation: The model predicts the correct translation by selecting the most probable sequence of words.
4.	Output Refinement: The generated translation is optimized to maintain natural fluency.

## Speech Recognition and Text-to-Speech

TSUYAKUGO! relies on two major components for speech processing:
A.	Speech Recognition - Google Speech-to-Text
TSUYAKUGO! uses Google's Speech Recognition API to convert spoken language into text. The process step is as follows:
1.	The microphone records audio.
2.	speech_recognition library processes the input.
3.	Google STT converts speech into text.
4.	The text is then passed to Mistral AI for translation.

B.	Text-to-Speech – Google Text-to-Speech/ gTTS
The system uses gTTS (Google Text-to-Speech) to convert the translated text into speech, making it easier for the user to understand. The process step is as follows:
1.	Mistral AI generates the translated text.
2.	gTTS converts the text into an audio file.
3.	PyGame plays the generated speech.

## Testing TSUYAKUGO!
TSUYAKUGO! is designed to be run locally on a user's machine, enabling real-time interpretation. The steps are as follows:
Step 1: Install Python
Install Python through python.org.
Step 2: Download Program Repository
Download program through uploaded files. Access the folder “TsuyakuGo” in command prompt or terminal.
Step 3: Install System Dependencies
Install dependencies with:
```
pip install -r requirements.txt
```
Step 4: Run Program Locally
Once all dependencies are installed and the repository is set up, run the program. First, navigate to the folder:
```
cd ./yourfoldername/TsuyakuGo/
```

Use your own API key from MistralAI, find how to create one from this:
https://docs.mistral.ai/getting-started/quickstart

Put your own API key at “config.py” file.
To run the speech-based interpretation program, run:
```
python tsuyakugo-speech.py
```
To run the text-based interpretation program, run:
```
python tsuyakugo-text.py
```
