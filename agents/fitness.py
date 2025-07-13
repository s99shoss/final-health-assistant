def suggest_fitness(weather_info):
    if weather_info and ("rain" in weather_info or "storm" in weather_info or "cold" in weather_info):
        return "🏋️ It's better to do indoor activities like yoga or stretching."
    else:
        return "🚶 Great day for a walk or outdoor jogging!"
