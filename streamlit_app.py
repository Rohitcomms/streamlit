import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        response = requests.post("https://dashboard.render.com/web/srv-ctrke33tq21c738tec8g/deploys/dep-ctrke3btq21c738tecb0", json={"url": url})
        if response.status_code == 200:
            st.subheader("Summary:")
            st.write(response.json()["summary"])
        else:
            st.error(response.json().get("error", "An error occurred."))
    else:
        st.error("Please enter a valid URL.")

