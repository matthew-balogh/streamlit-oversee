import streamlit as st
import os
import json

DETAILS_FILENAME = "details.json"
STORAGE_DIRURL = "storage"
CASES_DIRURL = f"{STORAGE_DIRURL}/cases"

st.set_page_config(
    page_title="Case Viewer",
    page_icon="assets/logo.png",
    layout="wide"
)

def get_case_details(id):
    case_details = None
    file_path = f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}"

    if os.path.isfile(file_path):
        with open(f"{CASES_DIRURL}/{id}/{DETAILS_FILENAME}") as f:
            case_details = json.load(f)
            f.close()

    return case_details

case_id = None

if "case_id" in st.query_params:
    case_id = st.query_params["case_id"]

if case_id is None and "last_interacted_case_id" in st.session_state:
    case_id = st.session_state["last_interacted_case_id"]
    st.query_params["case_id"] = case_id

if case_id is None:
    st.switch_page("pages/home.py")

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

    st.container(border=False, height=10)