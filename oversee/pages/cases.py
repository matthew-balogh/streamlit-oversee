import streamlit as st

from oversee.services.cases import new_case, get_cases
from oversee.utilities.paths import ASSETS_DIRURL

st.set_page_config(
    page_title="Manuscripts",
    page_icon=f"{ASSETS_DIRURL}/logo.png",
    layout="wide"
)

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
            st.switch_page("oversee/pages/case.py")

        for ind in additional_indicators:
            st.button("", key=f"{id}:indicator:{ind}", icon=ind, type="tertiary", disabled=True)

@st.dialog("New Manuscript")
def new_case_dialog():
    with st.form("newManuscriptForm", border=False):
        manuscript_title = st.text_input("Title")
        research_objective = st.text_input("Research Objective")

        st.container(height=5, border=False)

        with st.container(horizontal=True, horizontal_alignment="right"):
            submitted = st.form_submit_button("Create new Manuscript", type="primary")

            if submitted:
                if (manuscript_title is not None) and (len(manuscript_title) > 0) and (research_objective is not None) and (len(research_objective) > 0):
                    new_case(manuscript_title, research_objective)
                    st.rerun()
                else:
                    st.toast("Incomplete form!")

with st.container(horizontal=True, vertical_alignment="center"):
    st.header(":material/home_storage: Manuscripts")
    if st.button("Write new Manuscript", key="btn:newManuscript", icon=":material/history_edu:", type="primary"):
        new_case_dialog()

reversed_order = False
reversed_order_toggle = st.toggle("Recently created first")

st.html("<div style='margin-bottom: .75rem'></div>")

if reversed_order_toggle:
    reversed_order = True

case_list = sorted(get_cases(), key=lambda x: x["creation_timestamp"], reverse=reversed_order)

for case in case_list:
    create_case_list_elem(case)