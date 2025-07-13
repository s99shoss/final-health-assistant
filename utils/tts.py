from gtts import gTTS
import os
import platform
import re

# لیست زبان‌های پشتیبانی‌شده
SUPPORTED_LANGUAGES = ['en', 'de', 'fa']

def detect_language(text):
    """
    تشخیص ساده زبان متن بر اساس کلمات کلیدی و حروف خاص
    """
    if re.search(r'[\u0600-\u06FF]', text):  # حروف فارسی
        return 'fa'
    elif re.search(r'\b(und|ist|das|wetter|heute|gut)\b', text.lower()):
        return 'de'
    else:
        return 'en'

def speak(text, lang=None):
    if not lang:
        lang = detect_language(text)

    if lang not in SUPPORTED_LANGUAGES:
        print(f"⚠️ زبان '{lang}' پشتیبانی نمی‌شود. استفاده از انگلیسی.")
        lang = 'en'

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

        print(f"🔊 متن به صدا تبدیل شد ({lang}) و پخش شد.")
    except Exception as e:
        print(f"❌ خطای TTS: {str(e)}")
