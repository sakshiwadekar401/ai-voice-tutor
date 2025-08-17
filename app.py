import streamlit as st
import os
from utils import transcribe_audio, get_chatbot_response, text_to_speech_gtts

st.title("🎙️ Free AI Tutor (Offline Mode)")

# Upload audio
audio_file = st.file_uploader("Upload your question (MP3/WAV)", type=["mp3", "wav"])

if audio_file is not None:
    # Save file
    with open("input_audio.wav", "wb") as f:
        f.write(audio_file.read())

    st.audio("input_audio.wav")

    # Step 1: Speech → Text
    st.write("🔎 Transcribing...")
    question = transcribe_audio("input_audio.wav")
    st.write("**You asked:**", question)

    # Step 2: AI generates answer
    st.write("🤖 Thinking...")
    answer = get_chatbot_response(question)
    st.write("**AI Tutor says:**", answer)

    # Step 3: Convert Answer to Speech
    st.write("🔊 Generating audio...")
    output_path = text_to_speech_gtts(answer, "output.mp3")
    st.audio(output_path)
    st.write("**Audio response generated!** You can listen to it above.")