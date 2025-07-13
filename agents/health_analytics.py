from tinydb import TinyDB, Query

db = TinyDB("health_data.json")

def analyze_user_health(user_id):
    User = Query()
    records = db.search(User.user == user_id)

    if not records:
        return f"📭 No health data found for user '{user_id}'."

    systolic_list = []
    diastolic_list = []
    pulse_list = []

    for entry in records:
        if "blood_pressure" in entry:
            try:
                systolic, diastolic = map(int, entry["blood_pressure"].split("/"))
                systolic_list.append(systolic)
                diastolic_list.append(diastolic)
            except:
                continue
        if "pulse" in entry:
            pulse_list.append(entry["pulse"])

    avg_sys = sum(systolic_list) / len(systolic_list) if systolic_list else None
    avg_dia = sum(diastolic_list) / len(diastolic_list) if diastolic_list else None
    avg_pulse = sum(pulse_list) / len(pulse_list) if pulse_list else None

    result = f"📊 Health Analytics for {user_id}:\n"
    if avg_sys and avg_dia:
        result += f"🩺 Average Blood Pressure: {int(avg_sys)}/{int(avg_dia)} mmHg\n"
    if avg_pulse:
        result += f"💓 Average Pulse: {int(avg_pulse)} bpm"

    return result
