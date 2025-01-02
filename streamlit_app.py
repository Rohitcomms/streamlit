import streamlit as st
import requests

st.title("YouTube Video Transcript Summarizer")

url = st.text_input("Enter YouTube URL:")

if st.button("Get Summary"):
    if url:
        response = requests.post("https://flask-backend-5.onrender.com", json={"url": url})
        
        try:
            response.raise_for_status()
            response_json = response.json()
            
            if response.status_code == 200:
                st.subheader("Summary:")
                st.write(response_json.get("summary", "No summary available"))
            else:
                st.error(response_json.get("error", "An error occurred."))
        except requests.exceptions.RequestException as e:
            st.error(f"Request error: {e}")
        except ValueError:
            st.error("Error: Unable to parse response as JSON.")
    else:
        st.error("Please enter a valid URL.")
