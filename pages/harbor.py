import streamlit as st

st.header(":material/foundation: Welcome to the Harbor!")

st.info("The harbor shows your vessels, that is your existing projects.", icon=":material/foundation:")
st.warning("For now, your harbor is limited to a single vessel. For different projects, we recommend to clone a new Oversee repository and name it accordingly.", icon=":material/exclamation:")

with st.container(horizontal=True, vertical_alignment="center"):
    st.text("""
├┄┬┄┬┬┬┬      
├┴┄┴
""")
    st.page_link("pages/vessel.py", label="", icon=":material/sailing:")
    st.text("""
   ~            ~
≈                           ~            
            ~          ≈
~                   ~
""")