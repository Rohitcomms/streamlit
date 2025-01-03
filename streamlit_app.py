import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        backend_url = "https://dashboard.render.com/web/srv-ctrl7vlumphs73dvbu1g/deploys/dep-ctrl7vtumphs73dvbu60/summarize" 
        response = requests.post(backend_url, json={"url": url})
        
        if response.status_code == 200:
            st.subheader("Summary:")
            st.write(response.json()["summary"])
        else:
            st.error(response.json().get("error", "An error occurred."))
    else:
        st.error("Please enter a valid URL.")

