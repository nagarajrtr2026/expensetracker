import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FILE_PATH = os.path.join(BASE_DIR, "data", "expenses.json")

def load_data():
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)