import streamlit as st

st.set_page_config(
    page_title="Oversee",
    page_icon="assets/logo.png",
    layout="wide"
)

st.logo(
    "assets/logo_full.png",
    link="https://streamlit.io/gallery",
    icon_image="assets/logo.png",
    size="large"
)

pages = [
    st.Page("pages/welcome.py", title="Welcome"),
    st.Page("pages/home.py", title="Home", icon=":material/dashboard:", default=True),
    st.Page("pages/cases.py", title="Cases", icon=":material/home_storage:"),
]

pg = st.navigation(pages)
pg.run()