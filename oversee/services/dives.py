import os
import json

from datetime import datetime
from oversee.utilities.helpers_storage import DIVE_FILEPATH

def load_dive():
    if os.path.exists(DIVE_FILEPATH):
        with open(DIVE_FILEPATH, "r") as f:
            dive = json.load(f)
            f.close()
        return dive
    else: return None

def save_dive(text: str):
    entry = {"timestamp": datetime.now().isoformat(), "text": text}

    with open(DIVE_FILEPATH, "a") as f:
        json.dump(entry, f, indent=2)
        f.close()

def record_dive(filepath: str, dive):
    with open(filepath, "a") as f:
        json.dump(dive, f)
        f.write("\n")
        f.close()

def delete_dive():
    if os.path.exists(DIVE_FILEPATH):
        os.remove(DIVE_FILEPATH)