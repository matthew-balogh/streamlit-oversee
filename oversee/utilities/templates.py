import os
import shutil
import json

from pathlib import Path
from datetime import datetime
from oversee.utilities.paths import MANUSCRIPT_TEMPLATE_DIRURL, DETAILS_FILENAME, LAB_FILENAME

MANUSCRIPT_ID_PLACEHOLDER = "<OVERSEE_MANUSCRIPT_ID_PLACEHOLDER>"

def create_manuscript_from_template(manuscript_folder: Path, manuscript_id: str, title: str, objective: str):
    frm = MANUSCRIPT_TEMPLATE_DIRURL
    to = manuscript_folder

    if not os.path.exists(frm):
        print("Cannot copy. The template resource \"{frm}\" does not exist.")
        return

    if not os.path.exists(to):
        shutil.copytree(frm, to)

        lab_filepath = f"{to}/{LAB_FILENAME}"
        if os.path.exists(lab_filepath):
            with open(lab_filepath, "r") as f:
                data = f.read()
                f.close()
            data = data.replace("<OVERSEE_MANUSCRIPT_ID_PLACEHOLDER>", manuscript_id.replace("-", "‑"))
            with open(lab_filepath, "w") as f:
                f.write(data)
                f.close()

        details_filepath = f"{to}/{DETAILS_FILENAME}"
        if os.path.exists(details_filepath):
            with open(details_filepath, "r") as f:
                data = json.load(f)
                f.close()

            data["manuscript_id"] = manuscript_id
            data["manuscript_title"] = title
            data["research_objective"] = objective
            data["creation_timestamp"] = datetime.now().isoformat()

            with open(details_filepath, "w") as f:
                json.dump(data, f, indent=2)
                f.close()

    else:
        print(f"Cannot copy. The directory \"{to}\" already exists.")