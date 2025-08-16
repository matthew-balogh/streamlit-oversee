import streamlit as st
import os
import json

DETAILS_FILENAME = "details.json"
STORAGE_DIRURL = "storage"
CASES_DIRURL = f"{STORAGE_DIRURL}/cases"

st.set_page_config(
    page_title="Cases",
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

def create_case_list_elem(id, details):
    additional_indicators = []

    if details["research_result"]:
        additional_indicators.append(":material/lab_panel:")
    if details["future_directions"]:
        additional_indicators.append(":material/arrow_split:")

    with st.container(horizontal=True):
        st.button(details["case_title"], key=f"{id}:button", icon=":material/attach_file:", type="primary")
        for ind in additional_indicators:
            st.button("", key=f"{id}:indicator:{ind}", icon=ind, type="tertiary", disabled=True)


st.header(":material/home_storage: Cases")
st.html("<div style='margin-bottom: 1rem'></div>")

for case_id in os.listdir(CASES_DIRURL):
    case_details = get_case_details(case_id)

    if case_details is not None:
        create_case_list_elem(case_id, case_details)