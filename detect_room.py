import cv2

# Initialize Cascade Classifier object using a frontal face detection pre-trained model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Face counting function, which takes in image data
def count_faces(frame):

    # Greyscale image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(20, 20)
    )

    # Display detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    count = len(faces)
    cv2.putText(frame, f"Faces detected: {count}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam Face Counter", frame)

# Initialize camera capture
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop until escape key is pressed
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read frame.")
        break
    count_faces(frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
