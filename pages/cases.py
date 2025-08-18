import streamlit as st
import os
import json
import uuid

from helpers import is_demo_mode
from decorators import skip_if_demo
from helpers_templates import create_manuscript_from_template

DEMO_MODE = is_demo_mode()

DETAILS_FILENAME = "details.json"
STORAGE_DIRURL = "storage"
CASES_DIRURL = f"{STORAGE_DIRURL}/manuscripts"

st.set_page_config(
    page_title="Manuscripts",
    page_icon="assets/logo.png",
    layout="wide"
)

@skip_if_demo
def new_case(manuscript_title, research_objective):
    manuscript_id = uuid.uuid4()
    create_manuscript_from_template(manuscript_id, manuscript_title, research_objective)

def get_case_details(id):
    case_details = None
    file_path = f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}"

    if os.path.isfile(file_path):
        with open(f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}") as f:
            case_details = json.load(f)
            f.close()

    return case_details

def create_case_list_elem(details):
    id = details["manuscript_id"]
    additional_indicators = []

    if details["research_result"]:
        additional_indicators.append(":material/lab_panel:")
    if details["future_directions"]:
        additional_indicators.append(":material/arrow_split:")

    with st.container(horizontal=True):
        if st.button(details["manuscript_title"], key=f"{id}:button", icon=":material/contract:", type="primary"):
            st.session_state['last_interacted_case_id'] = id
            st.switch_page("pages/case.py")

        for ind in additional_indicators:
            st.button("", key=f"{id}:indicator:{ind}", icon=ind, type="tertiary", disabled=True)

@st.dialog("New Manuscript")
def new_case_dialog():
    with st.form("newManuscriptForm"):
        manuscript_title = st.text_input("Title")
        research_objective = st.text_input("Research Objective")

        submitted = st.form_submit_button("Create new Manuscript", type="primary")

        if submitted:
            if (manuscript_title is not None) and (len(manuscript_title) > 0) and (research_objective is not None) and (len(research_objective) > 0):
                new_case(manuscript_title, research_objective)
                st.rerun()
            else:
                st.toast("Incomplete form!")

with st.container(horizontal=True, vertical_alignment="center"):
    st.header(":material/home_storage: Manuscripts")
    if st.button("Write new Manuscript", key="btn:newManuscript", icon=":material/history_edu:", type="primary", disabled=DEMO_MODE):
        new_case_dialog()

reversed_order = False
reversed_order_toggle = st.toggle("Recently created first")

st.html("<div style='margin-bottom: .75rem'></div>")

if reversed_order_toggle:
    reversed_order = True

case_details_list = []

for case_id in os.listdir(CASES_DIRURL):
    case_details = get_case_details(case_id)

    if case_details is not None:
        case_details_list.append(case_details)

case_details_list = sorted(case_details_list, key=lambda x: x["creation_timestamp"], reverse=reversed_order)

for case_details in case_details_list:
    create_case_list_elem(case_details)