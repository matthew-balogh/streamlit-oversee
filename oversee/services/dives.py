import os
import json

from pathlib import Path
from datetime import datetime
from oversee.utilities.decorators import with_dive_filepath, with_manuscript_dives_filepath

@with_dive_filepath()
def load_dive(dive_filepath: Path = None):
    if os.path.exists(dive_filepath):
        with open(dive_filepath, "r") as f:
            dive = json.load(f)
            f.close()
        return dive
    else: return None

@with_dive_filepath()
def save_dive(text: str, dive_filepath: Path = None):
    entry = {"timestamp": datetime.now().isoformat(), "text": text}
    dive_filepath.parent.mkdir(exist_ok=True, parents=True)
    with open(dive_filepath, "a") as f:
        json.dump(entry, f, indent=2)
        f.close()

@with_dive_filepath()
def delete_dive(dive_filepath: Path = None):
    if os.path.exists(dive_filepath):
        os.remove(dive_filepath)

@with_manuscript_dives_filepath()
def record_dive(manuscript_id: str, dive: object, manuscript_dives_filepath: Path = None):
    with open(manuscript_dives_filepath, "a") as f:
        json.dump(dive, f)
        f.write("\n")
        f.close()