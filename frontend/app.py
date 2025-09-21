import os
import streamlit as st
import requests

st.title("OMR Evaluation System")

# Dropdown to select set
set_choice = st.selectbox("Select Set", ["SetA", "SetB"])

# Use container name inside Docker, fallback to localhost outside
backend_url = os.getenv("BACKEND_URL", "http://backend:8000/process-set/")

if st.button("Process Entire Set"):
    try:
        # Send POST request with selected set
        resp = requests.post(backend_url, json={"set_name": set_choice})
        if resp.status_code == 200:
            st.success("Processed successfully!")
            st.json(resp.json())
        else:
            st.error(f"Backend returned {resp.status_code}: {resp.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to backend: {e}")
