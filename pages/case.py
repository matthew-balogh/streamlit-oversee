import streamlit as st
import os
import json

from datetime import datetime
from pathlib import Path

DETAILS_FILENAME = "details.json"
LAB_FILENAME = "lab.py"
NOTES_FILENAME = "notes.md"
JOTS_FILENAME = "jots.jsonl"
STORAGE_DIRURL = "storage"
CASES_DIRURL = f"{STORAGE_DIRURL}/cases"

st.set_page_config(
    page_title="Case Viewer",
    page_icon="assets/logo.png",
    layout="wide"
)

def fragment_from_file(filepath: str):
    with open(filepath) as f:
        code = f.read()

    def run():
        exec(code, globals())

    return st.fragment(run)

def get_case_details(id):
    case_details = None
    file_path = f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}"

    if os.path.isfile(file_path):
        with open(f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}") as f:
            case_details = json.load(f)
            f.close()

    return case_details

def save_note(FILE: str, msg: str):
    with FILE.open("a", encoding="utf-8") as f:
        json.dump(
            {"ts": datetime.now().isoformat(), "msg": msg},
            f,
            ensure_ascii=False
        )
        f.write("\n")

def load_jots(FILE):
    if not FILE.exists():
        return []
    with FILE.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f]

case_id = None

if "case_id" in st.query_params:
    case_id = st.query_params["case_id"]

if case_id is None and "last_interacted_case_id" in st.session_state:
    case_id = st.session_state["last_interacted_case_id"]
    st.query_params["case_id"] = case_id

if case_id is None:
    st.switch_page("pages/home.py")

CASE_DIRURL = f"{STORAGE_DIRURL}/cases/{case_id}"
case_details = get_case_details(case_id)

with st.container():
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("Case:", type="tertiary", icon=":material/attach_file:", disabled=True)
        st.write(case_details['case_title'])
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("Research Objective:", type="tertiary", icon=":material/lab_research:", disabled=True)
        st.write(case_details['research_objective'])

    has_results = case_details['research_result']
    has_future_directions = case_details['future_directions']
    label_container = (st.container(horizontal=True) if (has_results or has_future_directions)
                        else st.empty())
    
    if has_results:
        label_container.info("Results are obtained", icon=":material/lab_panel:")
    
    if has_future_directions:
        label_container.warning("Future directions stated", icon=":material/arrow_split:")

    option_map = {
        0: ":material/science: Laboratory",
        1: ":material/book_5: Research Notes",
        2: ":material/lab_panel::material/arrow_split: Results and Future Directions"
    }

    selection = st.segmented_control(
        "",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
        default = 0
    )

    
    if selection == 0:
        lab_filepath = f"{CASE_DIRURL}/{LAB_FILENAME}"

        if not os.path.exists(lab_filepath):
            st.error(f"The '{LAB_FILENAME}' file is missing from storage", icon=":material/dangerous:")
            st.stop()

        lab_fragment = fragment_from_file(lab_filepath)
        lab_fragment()

    elif selection == 1:
        notes_filepath = f"{CASE_DIRURL}/{NOTES_FILENAME}"
        jots_filepath = f"{CASE_DIRURL}/{JOTS_FILENAME}"

        new_jot = st.chat_input("What to jot down?")
        if new_jot:
            save_note(Path(jots_filepath), new_jot)

        if not os.path.exists(notes_filepath):
            st.error(f"The '{NOTES_FILENAME}' file is missing from storage", icon=":material/dangerous:")
        else:
            notes_container = st.empty()

            def load_notes():
                with open(notes_filepath, "r") as f:
                    notes_container.empty()
                    notes_container.markdown(f.read())
                    f.close()

            load_notes()

        jots = load_jots(Path(jots_filepath))
        for jot in reversed(jots):
            st.chat_message("user").write(jot["msg"])