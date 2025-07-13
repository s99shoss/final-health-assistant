import requests

def get_weather(lat, lon):
    API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    try:
        res = requests.get(url)
        data = res.json()
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"🌤️ Weather is {temp}°C and {desc}."
    except:
        return "❌ Could not fetch weather data."
