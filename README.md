# 🧠 Multimodal AI Health Assistant Agent

A modular, voice-enabled AI health assistant system built using Python, FastAPI, and agent-based architecture.  
This project was developed as part of the **Dialogue Systems course (SS2025)** at the **University of Bonn**.

---

## 🚀 Features

- 🌤️ **Weather Agent** – Real-time weather data using OpenWeatherMap  
- 🏃 **Fitness Agent** – Activity suggestions based on weather  
- 🥗 **Nutrition Agent** – Nutrition info via `HealthcareAgent` API (USDA-calibrated)  
- 🧘 **Wellbeing Agent** – Mental wellness tips  
- 😴 **Sleep Agent** – Sleep analysis tips  
- ⏰ **Reminders Agent** – Health-related reminders  
- 📅 **Calendar Agent** – Event checking  
- 🤒 **Symptom Checker Agent** – Suggests potential health issues  
- 🩺 **Health Data Agent** – Logs blood pressure/pulse via TinyDB  
- 📊 **Health Analytics Agent** – Averages vitals for each user  
- 🌐 **Web Search Fallback** – Default response if no intent matched  
- 🔊 **TTS Output** – Speaks response using `gTTS`  
- 🧠 **Selector Agent** – Routes query to proper agents

---

## 📦 Installation

```bash
git clone https://github.com/your-username/final-health-assistant.git
cd final-health-assistant
pip install -r requirements.txt
```

### requirements.txt

```
fastapi
uvicorn
requests
gtts
tinydb
HealthcareAgent
```

---

## 🚀 Run the API

```bash
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

Use POST `/query/` endpoint to send queries.

---

## 🧪 Example Request

```json
{
  "query": "Tell me the weather and suggest a meal. Also analyze health report.",
  "location": {
    "lat": 35.7,
    "lon": 51.4
  },
  "user": "u1"
}
```

📤 Response might include:
- 🌤️ Current weather
- 🥗 USDA nutrition info via HealthcareAgent
- 📊 Health summary for user `u1`
- 🔊 Spoken response with gTTS

---

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
├── health_data.json
├── agents/
│   ├── weather.py
│   ├── fitness.py
│   ├── nutrition.py
│   ├── wellbeing.py
│   ├── sleep.py
│   ├── reminders.py
│   ├── calendar.py
│   ├── symptom.py
│   ├── health_data.py
│   ├── health_analytics.py
│   ├── websearch.py
│   └── selector.py
└── utils/
    ├── memory.py
    └── tts.py
```

---

## 👨‍💻 Contributors

- Mohammad Erfan Hosseini  
- Mohammad Mehdi Deylamipour  
- Amr Moustafa  
- Muhammad Zakria  

University of Bonn – Dialogue Systems – SS 2025

---

## 📝 License

This project is intended for educational and academic use only.
