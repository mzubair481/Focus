import cv2
import time
import ctypes
import screeninfo
from imutils.video import VideoStream

def get_display_centers():
    centers = []
    for display in screeninfo.get_monitors():
        center_x = display.x + display.width // 2
        center_y = display.y + display.height // 2
        centers.append((center_x, center_y))
        print(f"Display {display.name} center coordinates: ({center_x}, {center_y})")
    return centers

def move_mouse(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)

# Load pre-trained classifiers for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
face_detection_accuracy = 70

# Initialize video stream
vs = VideoStream(src=0).start()
time.sleep(2.0)  # Allow camera to warm up

# Get display centers
centers = get_display_centers()

# Assuming you want to use the first two displays' centers for face detection logic
if len(centers) >= 2:
    center1 = centers[0]
    center2 = centers[1]
else:
    print("Not enough displays detected.")
    center1 = (0, 0)
    center2 = (0, 0)

face_detected = False

try:
    while True:
        frame = vs.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=face_detection_accuracy, minSize=(30, 30))

        for (x, y, w, h) in faces:
            # Draw rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        if len(faces) > 0:
            # At least one face detected, assume user is facing the camera
            if not face_detected:
                move_mouse(*center1)
                face_detected = True
        else:
            # No face detected, assume user is looking away
            if face_detected:
                move_mouse(*center2)
                face_detected = False
        
        # Display the resulting frame
        cv2.imshow('Video', frame)
        key = cv2.waitKey(1) & 0xFF
        
        # Break the loop on 'q' key press
        if key == ord('q'):
            break
        
        # Add a small delay to prevent rapid switching
        time.sleep(0.1)

finally:
    # Cleanup
    cv2.destroyAllWindows()
    vs.stop()
