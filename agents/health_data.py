from tinydb import TinyDB

db = TinyDB("health_data.json")

def record_health_info(data):
    db.insert(data)
    return "🩺 Health data recorded successfully."
