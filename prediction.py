import streamlit as st
from ultralytics import YOLO
from PIL import Image

st.title("🚗 Vehicle Detection and Counting")

# Load YOLO model
model = YOLO("yolov8n.pt")

# Upload image
uploaded_file = st.file_uploader(
    "Upload a traffic image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    # Run YOLO detection
    results = model(image)

    # Display detected image
    annotated_image = results[0].plot()

    st.image(
        annotated_image,
        caption="Detected Vehicles",
        use_container_width=True
    )

    # Vehicle classes
    vehicle_classes = ["car", "motorcycle", "bus", "truck"]

    vehicle_count = {
        "car": 0,
        "motorcycle": 0,
        "bus": 0,
        "truck": 0
    }

    # Count vehicles
    for box in results[0].boxes:
        class_id = int(box.cls[0])
        class_name = model.names[class_id]

        if class_name in vehicle_classes:
            vehicle_count[class_name] += 1

    st.subheader("Vehicle Count")

    for vehicle, count in vehicle_count.items():
        st.write(f"**{vehicle.capitalize()}:** {count}")