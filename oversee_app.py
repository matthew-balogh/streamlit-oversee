import streamlit as st

from helpers import is_demo_mode, get_demo_banner_html, get_active_vessel_label_html

PRIMARY_COLOR = st.get_option('theme.primaryColor')
DEMO_MODE = is_demo_mode()

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
    st.Page("pages/landing.py", title="Come Aboard!", default=DEMO_MODE),

    st.Page("pages/harbor.py", title="Harbor", icon=":material/anchor:", default=(not DEMO_MODE)),
    st.Page("pages/vessel.py", title="Vessel", icon=":material/sailing:"),

    st.Page("pages/cases.py", title="Manuscripts", icon=":material/home_storage:"),
    st.Page("pages/case.py", title="Manuscript viewer", icon=":material/contract:"),
    st.Page("pages/help.py", title="Help", icon=":material/help:")
]

with navbar:
    with st.container(horizontal=True, horizontal_alignment="center", width=90):
        st.image("assets/logo.png", width=50)

    st.html("<div style='margin-bottom: 1rem'></div>")

    if DEMO_MODE:
        st.page_link(pages[0], icon=":material/hail:")

    st.page_link(pages[1], icon=":material/anchor:")
    st.page_link(pages[2], icon=":material/sailing:")
    additional_styling = f"""
        font-size: 12px;
        padding: 0;
        margin-left: .5rem;
        margin-bottom: .25rem;
        border-radius: .3rem;

        background: none;
        color: {PRIMARY_COLOR};
        opacity: 1;
    """
    st.html(get_active_vessel_label_html(id="navbar-vessel-label", styling=additional_styling))

    st.page_link(pages[3], icon=":material/home_storage:")
    st.page_link(pages[5], icon=":material/help:")

if DEMO_MODE:
    navbar.markdown(get_demo_banner_html(), unsafe_allow_html=True)
    
with panel:
    pg = st.navigation(pages, position="hidden")
    pg.run()