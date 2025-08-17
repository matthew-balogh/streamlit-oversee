import streamlit as st

from helpers import get_demo_banner_html

st.set_page_config(
    page_title="Oversee",
    page_icon="assets/logo.png",
    layout="wide"
)

main = st.container(horizontal=True)
navbar = main.container(horizontal_alignment="left", width=150)

placeholder = main.container(width=100)
placeholder.empty()

panel = main.container()

pages = [
    st.Page("pages/welcome.py", title="Welcome"),
    st.Page("pages/home.py", title="Harbor", icon=":material/anchor:", default=True),
    st.Page("pages/cases.py", title="Manuscripts", icon=":material/home_storage:"),
    st.Page("pages/case.py", title="Manuscript viewer", icon=":material/contract:"),
    st.Page("pages/help.py", title="Help", icon=":material/help:")
]

with navbar:
    with st.container(horizontal=True, horizontal_alignment="center", width=90):
        st.image("assets/logo.png", width=50)

    st.html("<div style='margin-bottom: 1rem'></div>")

    st.page_link(pages[1], icon=":material/anchor:")
    st.page_link(pages[2], icon=":material/home_storage:")
    st.page_link(pages[4], icon=":material/help:")

navbar.markdown(get_demo_banner_html(), unsafe_allow_html=True)
    
with panel:
    pg = st.navigation(pages, position="hidden")
    pg.run()