import streamlit as st
from tts import transcribe_voice, speak_text
import tempfile

st.set_page_config(page_title="Health Assistant Voice Chat", page_icon="🧠")
st.title("🧠 Health Assistant - Voice Interface")

st.markdown("🎙️ **Upload your voice (WAV)** and get intelligent responses. Supports **English** 🇬🇧 and **German** 🇩🇪.")

# Select language
lang = st.radio("Choose language for voice recognition and TTS:", ["en", "de"], index=0, horizontal=True)

# Upload audio
uploaded_audio = st.file_uploader("Upload your question as a .wav file", type=["wav"])

if uploaded_audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_audio.read())
        tmp_path = tmp.name

    st.audio(tmp_path, format="audio/wav")
    st.info("Transcribing audio...")

    query = transcribe_voice(tmp_path, language=lang)
    st.success(f"📝 Transcription: {query}")

    # Placeholder response (replace this with real response from agents)
    response = f"🤖 This is a placeholder response for: '{query}'"

    st.markdown(f"### 💬 Assistant: {response}")
    speak_text(response, language=lang)
