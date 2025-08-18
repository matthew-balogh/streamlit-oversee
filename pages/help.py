import streamlit as st
import os

WHATSNEW_FILEPATH = "pages/contents/whatsnew.md"

GETTING_STARTED_DIRURL = "pages/contents/getting-started"
GETTING_STARTED_OFFLINE_FILEPATH = f"{GETTING_STARTED_DIRURL}/offline.md"
GETTING_STARTED_ONLINE_FILEPATH = f"{GETTING_STARTED_DIRURL}/online.md"

st.subheader(":material/help: Help")

tab1, tab2, tab3 = st.tabs(["What's new on the Horizon", "Getting started", "Manuscript indicators"])

with tab1:
    if os.path.exists(WHATSNEW_FILEPATH):
        with open(WHATSNEW_FILEPATH, "r") as f:
            content = f.read()
            f.close()
        st.markdown(content, unsafe_allow_html=True)

with tab3:
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:research_results", icon=":material/lab_panel:", type="tertiary", disabled=True)
        st.write("This icon indicates that research results have been obtained for the manuscript.")
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:future_directions", icon=":material/arrow_split:", type="tertiary", disabled=True)
        st.write("This icon indicates that future directions have been stated for the manuscript.")

with tab2:
    option_map = {
        0: ":material/install_desktop: Running on your machine",
        1: ":material/cloud: Running on Streamlit"
    }

    selection = st.segmented_control(
        "",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
        default = 0
    )

    if selection == 0:
        if os.path.exists(GETTING_STARTED_OFFLINE_FILEPATH):
            with open(GETTING_STARTED_OFFLINE_FILEPATH, "r") as f:
                content = f.read()
                f.close()
            st.markdown(content)

        st.link_button("Go to repository", "https://github.com/matthew-balogh/streamlit-oversee", type="primary", icon=":material/folder_data:")

    if selection == 1:
        if os.path.exists(GETTING_STARTED_ONLINE_FILEPATH):
            with open(GETTING_STARTED_ONLINE_FILEPATH, "r") as f:
                content = f.read()
                f.close()
            st.markdown(content)