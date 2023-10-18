#计算人脸大小
import cv2
from ultralytics import YOLO

model = YOLO('yolov8n-face.pt')

# Initialize the video capture object (0 is usually the default camera)
cap = cv2.VideoCapture(0)


# Check if the camera is opened successfully
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=False)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()