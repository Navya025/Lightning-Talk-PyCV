import cv2
"""
Face & Eye Detection with OpenCV

Opens the default webcam, detects faces and eyes with Haar cascades in real time,
draws bounding boxes, and allows capturing a snapshot.

Controls:
  - 'c': Save current frame as 'captured_image.jpg'
  - 'q': Quit

Dependencies:
  - Python 3.8+
  - opencv-python

Usage:
  python face_eye_webcam.py

Notes:
  - Uses OpenCV's built-in haarcascade files via cv2.data.haarcascades.
  - Adjust detectMultiScale parameters (scaleFactor, minNeighbors) for your scene.
  - Ensure camera permissions are granted on your OS.
"""


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

       
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('Face and Eye Detection', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('c'):
        cv2.imwrite("captured_image.jpg", frame)
        print("Image saved as captured_image.jpg")

    
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
