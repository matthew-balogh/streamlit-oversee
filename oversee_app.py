import streamlit as st
import os
import json

from streamlit_lottie import st_lottie
from helpers import is_demo_mode, get_demo_banner_html, get_active_vessel_label_html

PRIMARY_COLOR = st.get_option('theme.primaryColor')
DEMO_MODE = is_demo_mode()

st.set_page_config(
    page_title="Oversee",
    page_icon="assets/logo.png",
    layout="wide"
)

@st.dialog(" ", width="small")
def open_anchor_down_dialog():
    c1, c2, c3 = st.columns([1, 10, 1])

    with c2:
        with st.container(horizontal_alignment="center"):
            st.html("""<span style="color: grey; font-size: 2rem; opacity: 0.5;">You are anchored down,<br>take a moment to think...</span>""", width="content")

            if os.path.exists("assets/pulse.json"):
                with open("assets/pulse.json", "r") as f:
                    data = json.load(f)
                    f.close()

                st_lottie(data, quality="high")

main = st.container(horizontal=True)
navbar = main.container(horizontal_alignment="left", width=150)

placeholder = main.container(width=100)
placeholder.empty()

panel = main.container()

pages = [
    st.Page("pages/landing.py", title="Come Aboard!", default=DEMO_MODE),

    st.Page("pages/harbor.py", title="Harbor", icon=":material/foundation:", default=(not DEMO_MODE)),
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

    st.page_link(pages[1], icon=":material/foundation:")
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

    st.container(height=5, border=False)

    st.button("Anchor down!", type="primary", icon=":material/anchor:", help="Take a moment to think!", on_click=open_anchor_down_dialog)

if DEMO_MODE:
    navbar.markdown(get_demo_banner_html(), unsafe_allow_html=True)
    
with panel:
    pg = st.navigation(pages, position="hidden")
    pg.run()