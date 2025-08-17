import streamlit as st

st.subheader(":material/help: Help")

tab1, tab2 = st.tabs(["Getting started", "Manuscript indicators"])

with tab1:
    st.warning("Limitation notice", icon=":material/warning:")
    st.write("While this demo gives you a quick feel for the tool, you can enjoy all its features by cloning the repository and running it locally.")
    st.write("By doing so, you will be able to directly modify the contents of different elements of a _manuscript_ such as the lab file, notes, results and future directions, along with creating new manuscripts.")
    
    st.write("For the detailed instructions to setup **Oversee**, visit the GitHub repository:")
    st.link_button("Go to repository", "https://github.com/matthew-balogh/streamlit-oversee", type="primary", icon=":material/folder_data:")

with tab2:
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:research_results", icon=":material/lab_panel:", type="tertiary", disabled=True)
        st.write("This icon indicates that research results have been obtained for the manuscript.")
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:future_directions", icon=":material/arrow_split:", type="tertiary", disabled=True)
        st.write("This icon indicates that future directions have been stated for the manuscript.")