import streamlit as st

from oversee.utilities.helpers_storage import ASSETS_DIRURL

st.set_page_config(
    page_title="Come Aboard!",
    page_icon=f"{ASSETS_DIRURL}/logo.png",
    layout="wide"
)

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    with st.container(horizontal=True, horizontal_alignment="left"):
        st.image(f"{ASSETS_DIRURL}/logo_wide.png", width=250)

    st.subheader("The compass for your Data Science experiments")
    st.write("Oversee your data experiments while in the harbor, stay focused and organized overseas, and share clear findings on return.")

    st.subheader("Get started on your machine", width=350)
    st.code("git clone https://github.com/matthew-balogh/streamlit-oversee.git oversee-my-data-science-project      ")
    st.code("""cd oversee-my-data-science-project
pip install -r requirements.txt
streamlit run oversee_app.py""")
    st.subheader(":balloon::tada: That's it! You are ready to *oversee* your Data Science project...")

    st.image(f"{ASSETS_DIRURL}/wave_background.png", use_container_width=True)