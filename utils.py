import whisper
from transformers import pipeline
import pyttsx3
from gtts import gTTS
import os

# Load Whisper model (tiny = fastest, medium/large = more accurate)
whisper_model = whisper.load_model("base")

# Load a Hugging Face text generation model
chatbot = pipeline("text-generation", model="distilgpt2")

# Whisper transcription
def transcribe_audio(audio_path: str) -> str:
    result = whisper_model.transcribe(audio_path)
    return result["text"]

# Chatbot response
def get_chatbot_response(prompt: str) -> str:
    response = chatbot(prompt, max_length=150, do_sample=True, top_p=0.9, temperature=0.7)
    return response[0]["generated_text"]

# Text-to-speech with pyttsx3
def text_to_speech_pyttsx3(text: str, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename

# Text-to-speech with gTTS (alternative)
def text_to_speech_gtts(text: str, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename
