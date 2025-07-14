from agents.weather import get_weather
from agents.fitness_agent import agent_fitness, prompt_fitness
from agents.wellbeing_agent import agent_wellbeing, prompt_wellbeing
from agents.nutrition_agent import agent_nutrition, prompt_nutrition
from agents.search_agent import agent_search, prompt_search
from agents.prompts import prompt_router
import re

def classify_input(agent_router, user_input: str) -> dict:
    full_prompt = prompt_router + f"\nUser Input: {user_input}"
    raw_output = agent_router.run(full_prompt)
    categories = re.findall(r'([A-Za-z]+):\n- (.+)', raw_output)
    output_dict = {cat: val.strip() for cat, val in categories}
    return output_dict

def route(user_input: str, location: dict, agent_router) -> list:
    ctx = {}
    responses = []

    weather_info = get_weather(location)
    if "error" not in weather_info:
        weather_text = f"{weather_info['city']}, {weather_info['temp']}°C, {weather_info['condition']}"
    else:
        weather_text = "Weather info unavailable"

    categories = classify_input(agent_router, user_input)

    for cat, sentence in categories.items():
        enriched = f"{prompt_router}\nWeather: {weather_text}\nUser: {sentence}"

        if cat == "Fitness":
            responses.append(agent_fitness.run(enriched))
        elif cat == "Wellbeing":
            responses.append(agent_wellbeing.run(enriched))
        elif cat == "Nutrition":
            responses.append(agent_nutrition.run(sentence))
        else:
            responses.append(agent_search.run(sentence))

    return responses
