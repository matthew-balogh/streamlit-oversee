import streamlit as st
import os
import json
import uuid

from streamlit_lottie import st_lottie

from oversee.services.dives import save_dive, load_dive
from oversee.utilities.paths import ASSETS_DIRURL
from oversee.utilities.helpers import is_demo_mode, get_demo_banner_html, get_active_vessel_label_html

PRIMARY_COLOR = st.get_option('theme.primaryColor')
DEMO_MODE = is_demo_mode()

st.set_page_config(
    page_title="Oversee",
    page_icon=f"{ASSETS_DIRURL}/logo.png",
    layout="wide"
)

if DEMO_MODE:
    if st.session_state.get("demo_session_id", None) is None:
        st.session_state["demo_session_id"] = f"demo_session-{str(uuid.uuid4())}"
        st.toast("Your demo session has been reset!", icon=":material/air_freshener:")

@st.dialog(" ", width="small")
def open_anchor_down_dialog():
    c1, c2, c3 = st.columns([1, 10, 1])

    with c2:
        with st.container(horizontal_alignment="center"):
            st.html("""<span style="color: grey; font-size: 2rem; opacity: 0.5;">You are anchored down,<br>take a moment to think...</span>""", width="content")

            if os.path.exists(f"{ASSETS_DIRURL}/pulse.json"):
                with open(f"{ASSETS_DIRURL}/pulse.json", "r") as f:
                    data = json.load(f)
                    f.close()

                st_lottie(data, quality="high")

@st.dialog(" ", width='large')
def open_dive_dialog():
    col1, col2, col3 = st.columns([.5, 30, .5], gap=None)

    with col2:
        st.html("""<span style="color: grey; font-size: 1.5rem; opacity: 0.9;">Vessel offshore?!<br>Don’t worry where to sail, just dive in and get aboard...</span>""", width="content")
        text = st.text_area("", placeholder="Start with your thoughts here...", label_visibility="collapsed", height="stretch")

        with st.container( horizontal_alignment="right"):
            if st.button("Dive in!", type="primary"):
                if text:
                    save_dive(text=text)
                    st.switch_page("oversee/pages/recent_dive.py")
                else:
                    st.toast("Incomplete form!")

main = st.container(horizontal=True)
navbar = main.container(horizontal_alignment="left", width=150)

placeholder = main.container(width=100)
placeholder.empty()

panel = main.container()

pages = [
    st.Page("oversee/pages/landing.py", title="Come Aboard!", default=DEMO_MODE),

    st.Page("oversee/pages/harbor.py", title="Harbor", icon=":material/foundation:", default=(not DEMO_MODE)),
    st.Page("oversee/pages/vessel.py", title="Vessel", icon=":material/sailing:"),
    st.Page("oversee/pages/recent_dive.py", url_path="recent-dive", title="Recent dive", icon=":material/pool:"),

    st.Page("oversee/pages/cases.py", title="Manuscripts", icon=":material/home_storage:"),
    st.Page("oversee/pages/case.py", title="Manuscript viewer", icon=":material/contract:"),
    st.Page("oversee/pages/help.py", title="Help", icon=":material/help:")
]

with navbar:
    with st.container(horizontal=True, horizontal_alignment="center", width=90):
        st.image(f"{ASSETS_DIRURL}/logo.png", width=50)

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

    st.page_link(pages[4], icon=":material/home_storage:")
    st.page_link(pages[6], icon=":material/help:")

    st.container(height=5, border=False)

    dive = load_dive()
    if dive is None:
        st.button("Dive!", type="primary", icon=":material/scuba_diving:", help="Just start!", on_click=open_dive_dialog)
    else:
        st.page_link(pages[3], icon=":material/pool:")

    st.button("Anchor down!", type="primary", icon=":material/anchor:", help="Take a moment to think!", on_click=open_anchor_down_dialog)

if DEMO_MODE:
    navbar.markdown(get_demo_banner_html(), unsafe_allow_html=True)
    
with panel:
    pg = st.navigation(pages, position="hidden")
    pg.run()