import os
import json
import uuid

from oversee.utilities.decorators import skip_if_demo
from oversee.utilities.helpers_templates import create_manuscript_from_template
from oversee.utilities.helpers_storage import MANUSCRIPTS_DIRURL, DETAILS_FILENAME

@skip_if_demo
def new_case(manuscript_title: str, research_objective: str):
    manuscript_id = str(uuid.uuid4())
    create_manuscript_from_template(manuscript_id, manuscript_title, research_objective)
    return manuscript_id

def get_case(id: str):
    case = None
    file_path = f"{MANUSCRIPTS_DIRURL}/{id}/{DETAILS_FILENAME}"

    if os.path.isfile(file_path):
        with open(f"{MANUSCRIPTS_DIRURL}/{id}/{DETAILS_FILENAME}") as f:
            case = json.load(f)
            f.close()

    return case