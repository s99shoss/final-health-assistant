from gtts import gTTS
import os
import platform

def speak(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        filename = "response.mp3"
        tts.save(filename)

        system = platform.system()
        if system == "Windows":
            os.system(f"start {filename}")
        elif system == "Darwin":
            os.system(f"afplay {filename}")
        else:
            os.system(f"xdg-open {filename}")
    except Exception as e:
        print("❌ TTS error:", str(e))
