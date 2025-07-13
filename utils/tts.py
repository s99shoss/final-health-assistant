import os
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def transcribe_voice(audio_file_path: str, language: str = "en") -> str:
    """
    Converts speech to text using Google Speech Recognition.

    Args:
        audio_file_path (str): Path to .wav file.
        language (str): 'en' for English, 'de' for German.

    Returns:
        str: Transcribed text or error message.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language=language)
    except sr.UnknownValueError:
        return "❌ Speech could not be understood."
    except sr.RequestError as e:
        return f"❌ API request error: {e}"


def speak_text(text: str, language: str = "en"):
    """
    Converts text to speech and plays the audio.

    Args:
        text (str): The text to speak.
        language (str): Language code ('en' or 'de').

    Returns:
        None
    """
    try:
        tts = gTTS(text=text, lang=language)
        tts.save("response.mp3")
        audio = AudioSegment.from_mp3("response.mp3")
        play(audio)
        os.remove("response.mp3")
    except Exception as e:
        print(f"❌ Error in text-to-speech: {e}")
