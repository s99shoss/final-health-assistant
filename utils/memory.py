from tinydb import TinyDB
db = TinyDB("memory.json")

def save_log(query, response):
    db.insert({"query": query, "response": response})
