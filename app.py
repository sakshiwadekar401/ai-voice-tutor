import streamlit as st
from modules import stt, tts, roleplay

st.set_page_config(page_title="AI Voice Tutor", page_icon="🎙️", layout="centered")

st.title("🎙️ AI Voice Tutor")
st.write("Practice speaking, listening, and roleplaying with AI.")

# Upload or record audio
uploaded_file = st.file_uploader("Upload your audio (wav format)", type=["wav"])

if uploaded_file:
    # Process Speech-to-Text
    st.write("🔍 Transcribing...")
    text = stt.transcribe_audio(uploaded_file)
    st.success(f"📝 You said: {text}")

    # Roleplay response
    st.write("🤖 Generating AI response...")
    reply = roleplay.get_ai_response(text)
    st.info(reply)

    # Text-to-Speech
    st.write("🔊 Speaking response...")
    tts.speak_text(reply)
    st.audio("output.wav", format="audio/wav")
