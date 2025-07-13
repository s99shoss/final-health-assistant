import requests
import os

OPENWEATHER_API_KEY = "7497f3f2038a79352308740208037d225"

def get_weather(location: dict) -> dict:
    """
    Fetch current weather from OpenWeatherMap.

    Args:
        location (dict): {'lat': float, 'lon': float}

    Returns:
        dict: weather info or error
    """
    lat = location.get("lat")
    lon = location.get("lon")
    if not lat or not lon:
        return {"error": "No coordinates provided"}

    try:
        res = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "lat": lat,
                "lon": lon,
                "appid": os.getenv("OPENWEATHER_API_KEY", OPENWEATHER_API_KEY),
                "units": "metric"
            },
            timeout=5
        ).json()

        return {
            "city": res.get("name", ""),
            "temp": res["main"]["temp"],
            "condition": res["weather"][0]["description"],
            "wind_kph": round(res["wind"]["speed"] * 3.6, 1)
        }
    except Exception as e:
        return {"error": str(e)}
