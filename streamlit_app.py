import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        response = requests.post("http://127.0.0.1:5000/process", json={"url": url})
        if response.status_code == 200:
            st.subheader("Summary:")
            st.write(response.json()["summary"])
        else:
            st.error(response.json().get("error", "An error occurred."))
    else:
        st.error("Please enter a valid URL.")

