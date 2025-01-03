import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

# Input box for the YouTube URL
url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        backend_url = "https://flsk-13.onrender.com/summarize"  # Replace with your actual Render URL

        try:
            # Send POST request to Flask backend
            response = requests.post(backend_url, json={"url": url})

            # Check for successful response
            if response.status_code == 200:
                st.subheader("Summary:")
                st.write(response.json()["summary"])
            else:
                # Display the error from the backend (e.g., subtitles disabled)
                st.error(f"Error from backend: {response.json().get('error', 'Unknown error')}")
        
        except requests.exceptions.RequestException as e:
            # Handle network errors
            st.error(f"Network error: {e}")
    else:
        st.error("Please enter a valid YouTube URL.")
