import streamlit as st

st.set_page_config(
    page_title="Traffic Monitoring System",
    page_icon="🚦",
    layout="wide"
)

st.title("🚦 YOLO-Based Traffic Monitoring System")

st.write(
    "A traffic monitoring system that uses YOLO to detect and count "
    "different types of vehicles from images and video streams."
)

st.subheader("Project Features")

st.write("🚗 Vehicle Detection and Counting")
st.write("📷 Image and Video Prediction")
st.write("💬 Traffic Rules Chatbot")
st.write("🚦 Road Signs and Driving Regulations")