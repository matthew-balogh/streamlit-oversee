import os
import shutil
import json

from datetime import datetime
from helpers_storage import MANUSCRIPTS_DIRURL, DETAILS_FILENAME, LAB_FILENAME

TEMPLATES_DIRURL = "_templates"
MANUSCRIPT_TEMPLATE_DIRURL = f"{TEMPLATES_DIRURL}/_manuscript"

MANUSCRIPT_ID_PLACEHOLDER = "<OVERSEE_MANUSCRIPT_ID_PLACEHOLDER>"

def create_manuscript_from_template(manuscript_id: str, title: str, objective: str):
    frm = MANUSCRIPT_TEMPLATE_DIRURL
    to = f"{MANUSCRIPTS_DIRURL}/{manuscript_id}"

    if not os.path.exists(frm):
        print("Cannot copy. The template resource \"{frm}\" does not exist.")
        return

    if not os.path.exists(to):
        shutil.copytree(frm, to)

        lab_filepath = f"{MANUSCRIPTS_DIRURL}/{manuscript_id}/{LAB_FILENAME}"
        if os.path.exists(lab_filepath):
            with open(lab_filepath, "r") as f:
                data = f.read()
                f.close()
            data = data.replace("<OVERSEE_MANUSCRIPT_ID_PLACEHOLDER>", manuscript_id.replace("-", "‑"))
            with open(lab_filepath, "w") as f:
                f.write(data)
                f.close()

        details_filepath = f"{MANUSCRIPTS_DIRURL}/{manuscript_id}/{DETAILS_FILENAME}"
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