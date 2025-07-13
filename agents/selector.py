def select_agents(query):
    query = query.lower()
    selected = []
    if "weather" in query or "temperature" in query:
        selected.append("weather")
    if "exercise" in query or "fitness" in query or "workout" in query:
        selected.append("fitness")
    if "meal" in query or "food" in query or "diet" in query or "nutrition" in query:
        selected.append("nutrition")
    if "stress" in query or "relax" in query or "wellbeing" in query or "mental" in query:
        selected.append("wellbeing")
    if "sleep" in query or "tired" in query or "rest" in query:
        selected.append("sleep")
    if "reminder" in query or "alarm" in query or "notify" in query:
        selected.append("reminders")
    if "schedule" in query or "calendar" in query or "event" in query:
        selected.append("calendar")
    if "symptom" in query or "fever" in query or "headache" in query or "nausea" in query or "cough" in query:
        selected.append("symptom")
    if "blood pressure" in query or "record health" in query:
        selected.append("health_data")
    if not selected:
        selected.append("websearch")
    return selected
