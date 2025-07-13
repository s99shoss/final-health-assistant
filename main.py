from fastapi import FastAPI, Request
from agents.weather import get_weather
from agents.fitness import suggest_fitness
from agents.nutrition import get_nutrition_recommendation
from agents.wellbeing import get_wellbeing_tip
from agents.sleep import analyze_sleep
from agents.reminders import get_reminders
from agents.calendar import check_calendar
from agents.websearch import fallback_response
from agents.selector import select_agents
from agents.symptom import analyze_symptoms
from agents.health_data import record_health_info
from agents.health_analytics import analyze_user_health
from utils.memory import save_log
from utils.tts import speak

app = FastAPI()

@app.post("/query/")
async def handle_query(req: Request):
    data = await req.json()
    query = data.get("query", "")
    location = data.get("location", {"lat": 35.7, "lon": 51.4})
    health_data_input = data.get("health_data", {})
    user_id = data.get("user", "default_user")

    selected = select_agents(query)
    responses = []

    weather_data = None
    if "weather" in selected:
        weather_data = get_weather(location["lat"], location["lon"])
        responses.append(weather_data)
    if "fitness" in selected:
        responses.append(suggest_fitness(weather_data))
    if "nutrition" in selected:
        responses.append(get_nutrition_recommendation(query))
    if "wellbeing" in selected:
        responses.append(get_wellbeing_tip())
    if "sleep" in selected:
        responses.append(analyze_sleep())
    if "reminders" in selected:
        responses.append(get_reminders())
    if "calendar" in selected:
        responses.append(check_calendar())
    if "symptom" in selected:
        responses.append(analyze_symptoms(query))
    if "health_data" in selected and health_data_input:
        responses.append(record_health_info(health_data_input))
    if "health_analytics" in selected:
        responses.append(analyze_user_health(user_id))
    if "websearch" in selected:
        responses.append(fallback_response())

    final_response = "\n".join(responses)
    save_log(query, final_response)
    speak(final_response)

    return {"response": final_response, "agents_used": selected}
