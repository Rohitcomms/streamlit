import streamlit as st
import requests
st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        # Replace with your Flask app's public URL
        response = requests.post("https://srv-ctrkp13tq21c738tjl1g.onrender.com/summarize", json={"youtube_url": url})
        
        if response.status_code == 200:
            st.subheader("Summary:")
            st.write(response.json()["summary"])  
        else:
            st.error(response.json().get("error", "An error occurred."))
    else:
        st.error("Please enter a valid YouTube URL.")

