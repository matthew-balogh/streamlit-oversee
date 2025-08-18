import streamlit as st
import os
import time

WHATSNEW_FILEPATH = "pages/contents/whatsnew.md"

GETTING_STARTED_DIRURL = "pages/contents/getting-started"
GETTING_STARTED_OFFLINE_FILEPATH = f"{GETTING_STARTED_DIRURL}/offline.md"
GETTING_STARTED_ONLINE_FILEPATH = f"{GETTING_STARTED_DIRURL}/online.md"

st.subheader(":material/help: Help")

tab_intro, tab_getting_started, tab_updates, tab_indicators = st.tabs(["I want to Oversee...", "Getting started", "What's new on the Horizon", "Manuscript indicators"])

with tab_updates:
    if os.path.exists(WHATSNEW_FILEPATH):
        with open(WHATSNEW_FILEPATH, "r") as f:
            content = f.read()
            f.close()
        st.markdown(content, unsafe_allow_html=True)

with tab_indicators:
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:research_results", icon=":material/lab_panel:", type="tertiary", disabled=True)
        st.write("This icon indicates that research results have been obtained for the manuscript.")
    with st.container(horizontal=True, vertical_alignment="center"):
        st.button("", key="help:indicator:future_directions", icon=":material/arrow_split:", type="tertiary", disabled=True)
        st.write("This icon indicates that future directions have been stated for the manuscript.")

with tab_getting_started:
    option_map = {
        0: ":material/install_desktop: Running on your machine",
        1: ":material/cloud: Running on Streamlit"
    }

    selection = st.segmented_control(
        "",
        options=option_map.keys(),
        format_func=lambda option: option_map[option],
        selection_mode="single",
        default = 0
    )

    if selection == 0:
        if os.path.exists(GETTING_STARTED_OFFLINE_FILEPATH):
            with open(GETTING_STARTED_OFFLINE_FILEPATH, "r") as f:
                content = f.read()
                f.close()
            st.markdown(content)

        st.link_button("Go to repository", "https://github.com/matthew-balogh/streamlit-oversee", type="primary", icon=":material/folder_data:")

    if selection == 1:
        if os.path.exists(GETTING_STARTED_ONLINE_FILEPATH):
            with open(GETTING_STARTED_ONLINE_FILEPATH, "r") as f:
                content = f.read()
                f.close()
            st.markdown(content)

with tab_intro:
    st.subheader("See how easy it is to *oversee* your experiments:")

    with st.chat_message("assistant"):
        st.write("Hi! It's me your personal assistant. How can I help you today?")
        time.sleep(1.5)

    with st.chat_message("user"):
        st.write("I would like to organize my **\"Introduction to Data Science\"** subject experiments, while tracking it in git. I work with notebooks, write notes and sometimes jot down my thoughts on my computer. I want to focus on specific problems in isolated environments while being able to oversee the whole progress.")
        time.sleep(2.5)

    with st.chat_message("assistant"):
        st.write("Then, you may try **Oversee**! Would you like me to set it up for you?")
        time.sleep(2)

    with st.chat_message("user"):
        st.write("Sure!")
        time.sleep(1.5)

    with st.chat_message("assistant"):
        with st.status("Creating your Oversee project...", expanded=True) as status:
            s = st.empty()
            s.write("⏳ Cloning `streamlit-oversee` from GitHub")
            time.sleep(3)
            s.write("✔️ Cloned `streamlit-oversee` from GitHub")

            s = st.empty()
            s.write("⏳ Renaming to `oversee-intro-to-data-science`")
            time.sleep(1)
            s.write("✔️ Renamed to `oversee-intro-to-data-science`")

            s = st.empty()
            s.write("⏳ Installing dependencies")
            time.sleep(3)
            s.write("✔️ Installed dependencies")

            s = st.empty()
            s.write("⏳ Starting your app")
            time.sleep(2)
            s.write("✔️ Started your app")

            s = st.empty()
            s.write("🎈🎉  Your Oversee app is available at `http://localhost:1234`")

            status.update(
                label="Oversee is now set up for your project!", state="complete", expanded=True
            )
    
    time.sleep(3)

    with st.chat_message("user"):
        st.write("That looks great! I think I'd like to *oversee* my **\"Master's Thesis\"** project in a similar environment.")
        time.sleep(1.5)

    with st.chat_message("assistant"):
        st.write("Say no more! I've got you covered!")
        time.sleep(2)

        with st.status("Creating another Oversee project for your Master's Thesis...", expanded=True) as status:
            s = st.empty()
            s.write("⏳ Cloning `streamlit-oversee` from GitHub")
            time.sleep(2)
            s.write("✔️ Cloned `streamlit-oversee` from GitHub")

            s = st.empty()
            s.write("⏳ Renaming to `oversee-masters-thesis`")
            time.sleep(1)
            s.write("✔️ Renamed to `oversee-masters-thesis`")

            s = st.empty()
            s.write("⏳ Installing dependencies")
            time.sleep(1)
            s.write("✔️ Installed dependencies")

            s = st.empty()
            s.write("⏳ Starting your app")
            time.sleep(1)
            s.write("✔️ Started your app")

            s = st.empty()
            s.write("🎈🎉  Your Oversee app is available at `http://localhost:1235`")

            status.update(
                label="Oversee is now set up for your Master's Thesis project!", state="complete", expanded=True
            )