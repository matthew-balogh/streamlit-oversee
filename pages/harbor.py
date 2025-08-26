import streamlit as st

from helpers import get_vessel_title

st.header(":material/foundation: Welcome to the Harbor!")
st.warning("For now, your harbor is limited to a single vessel. For different projects, we recommend to clone a new Oversee repository and name it accordingly.", icon=":material/warning:")
st.write("The harbor shows your vessels, that is your existing projects.")

vessel_title = get_vessel_title()

st.container(border=0, height=10)

with st.container(horizontal=True, vertical_alignment="top"):
    col1, col2 = st.columns([5, 10])

    with col1:
        st.text("├┄┬┄┬┬┬┬")
        st.page_link("pages/vessel.py", label=vessel_title, icon=":material/sailing:")
        st.text("├┴┄┴")
        
    with col2:
        with st.container(horizontal=True):
            for i in range(3):
                st.text("""
~            ~
≈                           ~            
            ~          ≈
~                   ~
""")