from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Pass classes=[67] to detect ONLY cell phones
    results = model(frame, classes=[67])

    annotated_frame = results[0].plot()

    cv2.imshow("Cellphone Detection Only", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
