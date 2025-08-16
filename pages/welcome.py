import streamlit as st

st.set_page_config(
    page_title="Welcome aboard Oversee",
    page_icon="assets/logo.png",
    layout="wide"
)

welcome_text_html = """
<span style="font-size: 1.5rem; font-style: italic;">Welcome aboard!</span>
"""

st.html("<div style='margin-bottom: 10rem'></div>")

with st.container(horizontal_alignment="center"):
    with st.container(horizontal=True, horizontal_alignment="center"):
        st.image("assets/logo_image_full.png", width=300)

    st.html(welcome_text_html, width="content")
    st.link_button("Sail overseas", type="primary", icon=":material/sailing:", url="/")