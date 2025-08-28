import streamlit as st

from oversee.services.dives import load_dive, delete_dive, record_dive
from oversee.services.cases import new_case, get_cases
from oversee.utilities.paths import ASSETS_DIRURL

st.set_page_config(
    page_title="Your recent dive...",
    page_icon=f"{ASSETS_DIRURL}/logo.png",
    layout="wide"
)

@st.dialog("New Manuscript")
def new_case_dialog(dive):
    with st.form("newManuscriptForm", border=False):
        manuscript_title = st.text_input("Title")
        research_objective = st.text_input("Research Objective")

        st.container(height=5, border=False)

        with st.container(horizontal=True, horizontal_alignment="right"):
            submitted = st.form_submit_button("Create new Manuscript", type="primary")

            if submitted:
                if (manuscript_title is not None) and (len(manuscript_title) > 0) and (research_objective is not None) and (len(research_objective) > 0):
                    case_id = new_case(manuscript_title, research_objective)
                    record_dive(manuscript_id=case_id, dive=dive)
                    delete_dive()
                    st.switch_page("oversee/pages/cases.py")
                else:
                    st.toast("Incomplete form!")

@st.dialog("Attach to Manuscript", width="large")
def attach_to_case_dialog(dive):
    reversed_order = False
    reversed_order_toggle = st.toggle("Recently created first")

    if reversed_order_toggle:
        reversed_order = True
    
    case_list = sorted(get_cases(), key=lambda x: x["creation_timestamp"], reverse=reversed_order)
    selection = st.pills("Selected Manuscript", case_list, format_func=lambda option: f":material/contract: {option['manuscript_title']}", selection_mode="single", label_visibility="hidden")

    st.container(height=5, border=False)

    with st.container(horizontal=True, horizontal_alignment="right"):
        if st.button("Attach to Manuscript", type="primary", disabled=(not selection)):
            case_id = selection["manuscript_id"]
            record_dive(manuscript_id=case_id, dive=dive)
            delete_dive()
            st.switch_page("oversee/pages/cases.py")

@st.dialog("Return to shore?")
def dismiss_dive_dialog():
    st.container(height=2, border=False)
    with st.container(horizontal=True, horizontal_alignment="right"):
        
        dismiss = st.button("Return ashore (delete dive)!", icon=":material/cancel:", type="tertiary")
        back = st.button("Keep swimming!", type="primary")

        if dismiss:
            delete_dive()
            st.switch_page("oversee/pages/harbor.py")
        
        if back:
            st.rerun()

def create_case_list_elem(details):
    id = details["manuscript_id"]

    with st.container(horizontal=True):
        if st.button(details["manuscript_title"], key=f"{id}:button", icon=":material/contract:", type="primary"):
            return id


recent_dive = load_dive()

if recent_dive is None:
    st.stop()

col1, col2, col3 = st.columns([1, 10, 8], gap="large")

with col2:
    st.header(":material/pool: Your recent dive:")

    with st.container(border=True):
        st.text(recent_dive["text"])

with col3:
    st.header(" ")

    with st.container(height="stretch", vertical_alignment="center"):
        if st.button("Write new Manuscript", icon=":material/history_edu:", type="primary"):
            new_case_dialog(recent_dive)

        if st.button("Attach to existing Manuscript", icon=":material/attach_file:", type="primary"):
            attach_to_case_dialog(recent_dive)

        if st.button("Return to shore!", icon=":material/barefoot:", type="tertiary"):
            dismiss_dive_dialog()