
import json
from datetime import datetime

DB_PATH = "db.json"

def load_db():
    try:
        with open(DB_PATH, "r") as f:
            return json.load(f)
    except:
        return {"mood_log": [], "goals": []}

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def log_mood(feeling):
    db = load_db()
    db["mood_log"].append({
        "feeling": feeling,
        "timestamp": datetime.now().isoformat()
    })
    save_db(db)

def set_goal(goal_text):
    db = load_db()
    db["goals"].append({
        "goal": goal_text,
        "created": datetime.now().isoformat(),
        "status": "active"
    })
    save_db(db)

def get_goals():
    db = load_db()
    return db["goals"][-3:]
