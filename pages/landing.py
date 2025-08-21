import streamlit as st

st.set_page_config(
    page_title="Come Aboard!",
    page_icon="assets/logo.png",
    layout="wide"
)

intro_html = """
<style>
    #landing-intro-text {
        display: block;
        margin-top: 2rem;
        color: #8195ac;
        font-size: 1.6rem;

        .highlighted {
            color: #416793;
        }
    }
</style>

<span id="landing-intro-text">
    <span class="highlighted">Oversee</span> your <span class="highlighted">data experiments</span> while in the harbor,<br>stay focused and organized overseas, and share clear findings on return.
</span>
"""

col1, col2, col3 = st.columns([1, 10, 1])

with col2:
    with st.container(horizontal=True, horizontal_alignment="left"):
        st.image("assets/logo_image_full_wo_padding.png")

    st.markdown(intro_html, width=600, unsafe_allow_html=True)
    st.container(height=25, border=False)

    c1, c2 = st.columns([3, 2], gap="large")

    with c1:
        st.header("Get started on your machine", width=300)
        st.container(height=5, border=False)
        st.code("git clone https://github.com/matthew-balogh/streamlit-oversee.git oversee-my-data-science-project      ")
        st.code("""cd oversee-my-data-science-project
pip install -r requirements.txt
streamlit run oversee_app.py""")
    
    with c2:
        st.header("Get started in the Cloud", width=300)
        st.container(height=5, border=False)
        st.link_button(icon=":material/cloud:", label="Fork the app in Streamlit Cloud*", url="https://share.streamlit.io/create-from-fork?owner=matthew-balogh&repository=streamlit-oversee&branch=main&mainModule=oversee_app.py&appId=e533f03e-7091-49cb-aa90-bd47b22c29cc", type="primary")

    st.container(height=10, border=False)
    st.subheader(":balloon::tada: That's it! You are ready to *oversee* your Data Science project...")

    st.container(height=25, border=False)
    st.caption("\*  You can keep separate Oversee projects on your computer, but in the cloud, forking only gives you one copy. For now, if you want to keep your projects isolated, we recommend starting on your machine.")

st.image("assets/waves_background.png", use_container_width=True)