from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

# Vehicle class IDs in COCO dataset: car(2), motorcycle(3), bus(5), truck(7)
vehicle_classes = [2, 3, 5, 7]

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Pass classes=vehicle_classes to detect ONLY vehicles
    results = model(frame, classes=vehicle_classes, conf=0.35)

    annotated_frame = results[0].plot()

    cv2.imshow("Vehicle Detection Only", annotated_frame)

    # Press 'q' to exit the loop and close the camera
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()