import os
import json

from pathlib import Path
from oversee.utilities.decorators import with_new_manuscript_id, with_manuscript_folder, with_manuscript_parent_folders
from oversee.utilities.templates import create_manuscript_from_template
from oversee.utilities.paths import DETAILS_FILENAME

@with_manuscript_folder()
def get_manuscript_folder(manuscript_id: str, manuscript_folder: Path = None):
    return manuscript_folder

@with_new_manuscript_id()
@with_manuscript_folder()
def new_case(manuscript_title: str, research_objective: str, manuscript_folder: Path = None, manuscript_id: str = None):
    create_manuscript_from_template(manuscript_folder, manuscript_id, manuscript_title, research_objective)
    return manuscript_id

@with_manuscript_parent_folders()
def get_cases(manuscript_parent_folders: list[Path] = None):
    cases = []
    for dirurl in manuscript_parent_folders:
        if os.path.exists(dirurl):
            for manuscript_id in filter(lambda x: not str(x).startswith("demo-session-"), os.listdir(dirurl)):
                case = get_case(manuscript_id=manuscript_id)
                if case is not None:
                    cases.append(case)
    return cases

@with_manuscript_folder()
def get_case(manuscript_id: str, manuscript_folder: Path = None):
    case = None
    file_path = f"{manuscript_folder}/{DETAILS_FILENAME}"
    if os.path.isfile(file_path):
        with open(file_path) as f:
            case = json.load(f)
            f.close()
    return case