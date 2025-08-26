import streamlit as st
import os
import json

from oversee.utilities.helpers import is_demo_mode
from oversee.utilities.helpers_storage import ASSETS_DIRURL, DIVES_FILENAME, DETAILS_FILENAME, LAB_FILENAME, STORAGE_DIRURL, NOTES_FILENAME, JOTS_FILENAME, RESULTS_FILENAME, FUTURE_DIRECTIONS_FILENAME

from oversee.utilities.decorators import fallback_to_session_storage_read_in_demo, fallback_to_session_storage_write_in_demo
from datetime import datetime

DEMO_MODE = is_demo_mode()

st.set_page_config(
    page_title="Manuscript Viewer",
    page_icon=f"{ASSETS_DIRURL}/logo.png",
    layout="wide"
)

case_id = None

if "case_id" in st.query_params:
    case_id = st.query_params["case_id"]

if case_id is None and "last_interacted_case_id" in st.session_state:
    case_id = st.session_state["last_interacted_case_id"]
    st.query_params["case_id"] = case_id

if case_id is None:
    st.switch_page("oversee/pages/cases.py")

CASE_DIRURL = f"{STORAGE_DIRURL}/manuscripts/{case_id}"
DETAILS_FILEPATH = f"{CASE_DIRURL}/{DETAILS_FILENAME}"
DIVES_FILEPATH = f"{CASE_DIRURL}/{DIVES_FILENAME}"
LAB_FILEPATH = f"{CASE_DIRURL}/{LAB_FILENAME}"
NOTES_FILEPATH = f"{CASE_DIRURL}/{NOTES_FILENAME}"
JOTS_FILEPATH = f"{CASE_DIRURL}/{JOTS_FILENAME}"
RESULTS_FILEPATH = f"{CASE_DIRURL}/{RESULTS_FILENAME}"
FUTURE_DIRECTIONS_FILEPATH = f"{CASE_DIRURL}/{FUTURE_DIRECTIONS_FILENAME}"

def get_case_details():
    case_details = None
    filepath = DETAILS_FILEPATH

    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            case_details = json.load(f)
            f.close()

    return case_details

def get_lab_renderer():
    with open(LAB_FILEPATH, "r") as f:
        lab = f.read()
        f.close()

    def run():
        exec(lab, globals())

    return st.fragment(run)

def load_notes():
    notes = None
    with open(NOTES_FILEPATH, "r") as f:
        notes = f.read()
        f.close()
    return notes

def load_dives():
    dives = []
    if os.path.exists(DIVES_FILEPATH):
        with open(DIVES_FILEPATH, "r") as f:
            dives = [json.loads(line) for line in f]
            f.close()
    return dives

@fallback_to_session_storage_read_in_demo(session_key=f"{case_id}.jots")
def load_jots():
    jots = []
    if os.path.exists(JOTS_FILEPATH):
        with open(JOTS_FILEPATH, "r") as f:
            jots = [json.loads(line) for line in f]
            f.close()
    return jots

def save_jot(jot: str):
    entry = {"timestamp": datetime.now().isoformat(), "jot": jot}

    @fallback_to_session_storage_write_in_demo(session_parent_key=f"{case_id}.jots", session_entry_key=entry["timestamp"], entry=entry)
    def save_jot_entry(entry):
        with open(JOTS_FILEPATH, "a") as f:
            json.dump(entry, f)
            f.write("\n")
            f.close()
    
    save_jot_entry(entry)


case_details = get_case_details()

if case_details is None:
    st.switch_page("oversee/pages/cases.py")

with st.container():
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("Manuscript:", type="tertiary", icon=":material/contract:", disabled=True, help=f":material/barcode:  {case_details['manuscript_id']}")
        st.write(case_details['manuscript_title'])
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("Research Objective:", type="tertiary", icon=":material/lab_research:", disabled=True)
        st.write(case_details['research_objective'])

    has_results = case_details['research_result']
    has_future_directions = case_details['future_directions']
    label_container = (st.container(horizontal=True) if (has_results or has_future_directions)
                        else st.empty())
    
    if has_results:
        label_container.info("Results are obtained", icon=":material/lab_panel:", width=200)
    
    if has_future_directions:
        label_container.warning("Future directions stated", icon=":material/arrow_split:", width=225)

    dives = load_dives()
    for dive in dives:
        st.info(dive.get("text"), icon=":material/scuba_diving:")

    option_map = {
        0: ":material/science: Cabin Laboratory",
        1: ":material/book_5: Journal",
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
        if os.path.exists(LAB_FILEPATH):
            renderer = get_lab_renderer()
            renderer()
        else:
            st.error(f"The '{LAB_FILENAME}' file is missing from storage", icon=":material/dangerous:")
            st.stop()

    elif selection == 1:
        new_jot = st.chat_input("What to jot down?")

        if os.path.exists(NOTES_FILEPATH):
            notes = load_notes()
            notes_container = st.empty()
            notes_container.markdown(notes, unsafe_allow_html=True)
        else:
            st.error(f"The '{NOTES_FILENAME}' file is missing from storage", icon=":material/dangerous:")

        if new_jot:
            save_jot(new_jot)

        if os.path.exists(JOTS_FILEPATH):
            for jot in reversed(load_jots(JOTS_FILEPATH, case_id)):
                st.chat_message("user").write(jot["jot"])

    elif selection == 2:
                col1, col2 = st.columns(spec=[0.55, 0.45])

                with col1:
                    st.subheader(":material/lab_panel: Results")

                    if case_details["research_result"]:
                        if os.path.exists(RESULTS_FILEPATH):
                            with open(RESULTS_FILEPATH, "r") as f:
                                content = f.read()
                                f.close()
                            st.info(content)
                        else:
                            st.error("The results are missing")
                    else:
                        st.caption("There are no results yet")

                with col2:
                    st.subheader(":material/arrow_split: Future Directions")

                    if case_details["future_directions"]:
                        if os.path.exists(FUTURE_DIRECTIONS_FILEPATH):
                            with open(FUTURE_DIRECTIONS_FILEPATH, "r") as f:
                                content = f.read()
                                f.close()
                            st.warning(content)
                        else:
                            st.error("The future directions are missing")
                    else:
                        st.caption("There are no future directions yet")