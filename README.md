# 🧠 Multimodal AI Health Assistant Agent

A modular, voice-enabled AI health assistant system built using Python, FastAPI, and LLM-style agents.  
This project was developed as part of the **Dialogue Systems course (SS2025)** at the **University of Bonn**.

## 🚀 Features

- 🌤️ Weather Agent – Real-time weather data using OpenWeatherMap  
- 🏃 Fitness Agent – Smart fitness advice based on weather  
- 🥗 Nutrition Agent – Healthy meal suggestions  
- 🧘 Wellbeing Agent – Mental wellness tips  
- 😴 Sleep Agent – Simple sleep tracking and advice  
- ⏰ Reminders Agent – Personal health reminders  
- 📅 Calendar Agent – Health-related event reminders  
- 🌐 Web Search Fallback – Generic fallback for unmatched queries  
- 🧠 Selector Agent – Auto-routing queries to proper agents  
- 🔊 TTS (Text-to-Speech) output using gTTS  
- 🗃️ TinyDB for simple memory logging  

## 📦 Installation

Install dependencies:

```
pip install -r requirements.txt
```

## 🚀 Run the API

Start the FastAPI server:

```
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

Use the POST `/query` endpoint to test the agent system.

## 🧾 Example Request

```json
{
  "query": "Suggest me a meal and tell me the weather in Tehran",
  "location": {
    "lat": 35.7,
    "lon": 51.4
  }
}
```

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
├── agents/
│   ├── weather.py
│   ├── fitness.py
│   ├── nutrition.py
│   ├── wellbeing.py
│   ├── sleep.py
│   ├── reminders.py
│   ├── calendar.py
│   ├── websearch.py
│   └── selector.py
└── utils/
    ├── memory.py
    └── tts.py
```

## 👨‍💻 Contributors

- Mohammad Erfan Hosseini  
- Mohammad Mehdi Deylamipour  
- Amr Moustafa  
- Muhammad Zakria  

University of Bonn – Dialogue Systems – SS 2025

## 📝 License

This project is intended for educational and academic purposes only.
