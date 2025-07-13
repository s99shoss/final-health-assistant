import os
import requests
import re
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, tool, Tool

# -------------------------------------
# CONFIGURATION
OPENWEATHER_API_KEY = "7497f3f2038a79352308740208037d225"
SPOONACULAR_API_KEY = "f2f6b1736b0e488d9bf536af6b017519"
BASE_URL = "https://api.spoonacular.com"

categories = ['Weather', 'Fitness', 'Wellbeing', 'Sleep', 'Calendar', 'Nutrition', 'Reminder', 'Search', 'Unknown']

# -------------------------------------
# WEATHER TOOL
@tool
def get_weather(data: dict, ctx: dict) -> dict:
    loc = data.get('location', {})
    lat = loc.get('lat')
    lon = loc.get('lon')
    if lat is None or lon is None:
        return {"error": "Location not provided"}
    key = os.getenv("OPENWEATHER_API_KEY", OPENWEATHER_API_KEY)
    try:
        r = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"lat": lat, "lon": lon, "units": "metric", "appid": key},
            timeout=5
        ).json()
        info = {
            "city": r.get("name", ""),
            "temp": r["main"]["temp"],
            "condition": r["weather"][0]["description"],
            "wind_kph": round(r["wind"]["speed"] * 3.6, 1)
        }
    except Exception as e:
        return {"error": str(e)}
    ctx['weather'] = info
    return info

# -------------------------------------
# SPOONACULAR TOOL
class SpoonacularTool(Tool):
    inputs = {
        "input_text": {
            "type": "string",
            "description": "Command: 'search:' or 'details:'"
        }
    }
    output_type = "string"
    name = "SpoonacularTool"
    description = "Search recipes or fetch details using Spoonacular API"

    def forward(self, input_text: str) -> str:
        command, _, arg = input_text.partition(":")
        if command == "search":
            return self.search_recipes(arg)
        if command == "details":
            return self.get_full_details(arg)
        return f"Unknown command: {input_text}"

    def search_recipes(self, query: str, number: int = 3) -> str:
        url = f"{BASE_URL}/recipes/complexSearch"
        params = {
            'query': query,
            'number': number,
            'addRecipeInformation': False,
            'apiKey': SPOONACULAR_API_KEY
        }
        resp = requests.get(url, params=params)
        resp.raise_for_status()
        results = resp.json().get('results', [])
        return "\n".join(f"{r['id']}: {r['title']}" for r in results)

    def get_full_details(self, recipe_id: str) -> str:
        instr = requests.get(
            f"{BASE_URL}/recipes/{recipe_id}/analyzedInstructions",
            params={'apiKey': SPOONACULAR_API_KEY}
        ).json()
        steps = [step['step'] for section in instr for step in section.get('steps', [])]
        nut = requests.get(
            f"{BASE_URL}/recipes/{recipe_id}/nutritionWidget.json",
            params={'apiKey': SPOONACULAR_API_KEY}
        ).json()
        taste = requests.get(
            f"{BASE_URL}/recipes/{recipe_id}/tasteWidget.json",
            params={'apiKey': SPOONACULAR_API_KEY}
        ).json()
        out = "**Instructions:**\n"
        for i, s in enumerate(steps, 1): out += f"{i}. {s}\n"
        out += "\n**Nutrition per serving:**\n"
        out += f"- Calories: {nut['calories']}\n- Carbs: {nut['carbs']}\n- Fat: {nut['fat']}\n- Protein: {nut['protein']}\n"
        out += "\n**Taste Profile:**\n"
        for k, v in taste.items(): out += f"- {k.capitalize()}: {v}%\n"
        return out

# -------------------------------------
# PROMPTS
def generate_prompt(name, purpose, capabilities, returns, final_only=True):
    parts = [
        f"You are {name}.",
        f"Purpose: {purpose}",
        "Capabilities:",
        *[f"- {c.strip()}" for c in capabilities.split(';') if c.strip()],
        "Returns:",
        *[f"- {r.strip()}" for r in returns.split(';') if r.strip()],
        "Only output the final result in plain text."
    ]
    if final_only:
        parts.append("Do not show any code, plan, or explanation.")
    parts.append("If you cannot respond, return 'NO_RESPONSE'.")
    return "\n".join(parts)

prompt_router = """You are a classification assistant. Your ONLY task is to analyze user's paragraph then split it into parts then categorize them based on the categories provided using their description.
...
"""  # برای brevity کاملش توی پیام قبلی هست

prompt_wellbeing = generate_prompt("Wellbeing Companion", "Support mental wellness.", "Analyze emotional tone", "Advice")
prompt_fitness = generate_prompt("Fitness Coach", "Workout recommendations", "Recommend activities", "Personal fitness plan")
prompt_search = generate_prompt("Search Assistant", "Answer general queries", "Use DuckDuckGo", "Factual answer")
prompt_nutrition = (
    "You are an expert cooking assistant. ... (همون کامل شده‌ای که ارسال کردیم قبلاً)"
)

# -------------------------------------
# AGENTS
model = LiteLLMModel(model_id="ollama/qwen2.5-coder:3b")
agent_router = CodeAgent(model=model, tools=[], max_steps=3, prompt_templates={"system_prompt": prompt_router})
agent_wellbeing = CodeAgent(model=model, tools=[], max_steps=2, prompt_templates={"system_prompt": prompt_wellbeing})
agent_fitness = CodeAgent(model=model, tools=[get_weather], max_steps=2, prompt_templates={"system_prompt": prompt_fitness})
agent_search = CodeAgent(model=model, tools=[DuckDuckGoSearchTool()], max_steps=2, prompt_templates={"system_prompt": prompt_search})
agent_nutrition = CodeAgent(model=model, tools=[SpoonacularTool(), DuckDuckGoSearchTool()], max_steps=2)
agent_nutrition.prompt_templates['system_prompt'] = prompt_nutrition

# -------------------------------------
# ROUTER FUNCTION
def router(user_input: str, location: dict) -> str:
    ctx = {}
    weather_info = get_weather({"location": location}, ctx)
    weather_text = (
        f"Weather in {weather_info['city']}: {weather_info['temp']}°C, {weather_info['condition']}"
        if "error" not in weather_info else "Weather unavailable"
    )

    full_prompt = prompt_router + "\nUser Input: " + user_input
    output_raw = agent_router.run(full_prompt)

    print("\n[Router Output]\n", output_raw)

    # You can extract categories and route them to other agents here...

# -------------------------------------
# TEST
if __name__ == "__main__":
    sample_input = "I want to eat something rich in protein, go to the gym, and know the weather in Berlin today."
    location = {'lat': 52.52, 'lon': 13.4050}  # Berlin
    router(sample_input, location)
