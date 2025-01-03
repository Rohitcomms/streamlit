import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        backend_url = "http://127.0.0.1:10000/summarize" 
        try:
            
            response = requests.post(backend_url, json={"url": url})

            if response.status_code == 200:
                st.subheader("Summary:")
                st.write(response.json()["summary"])
            else:
            
                st.error(response.json().get("error", "An error occurred."))
        except requests.exceptions.RequestException as e:
           
            st.error(f"Network error: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")


