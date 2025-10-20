# Face & Eye Detection using OpenCV

This project uses **OpenCV’s Haar Cascade Classifiers** to perform **real-time face and eye detection** via your webcam. It also allows you to **capture snapshots** of the video feed.

---

## Features

* Real-time **group face detection** using Haar cascades
* Automatically opens your **default webcam** (`VideoCapture(0)`)
* **Draws bounding boxes** around detected faces
* **Displays** total number of faces detected
---

## Requirements

* Python 3.8 or later
* OpenCV library

Install OpenCV using pip:

```bash
pip install opencv-python
```

---

## How to Run

1. Clone or download this repository.
2. Run it using:

   ```bash
   python detect_room.py
   ```
3. A window will open showing the webcam feed.

   * Press **`esc`** to quit the program

---

## Code Overview

```python
import cv2

# Load pre-trained Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

...

# Initialize webcam
cap = cv2.VideoCapture(0)
```

1. **Cascade Loading** – Loads the Haar cascade XML files that contain pre-trained models for detecting faces and eyes.
2. **Video Stream** – Opens your webcam using `cv2.VideoCapture(0)`.
3. **Frame Loop** – Continuously reads frames, converts them to grayscale, and runs `detectMultiScale()` to find faces and eyes.
4. **Drawing & Display** – Rectangles are drawn around detected regions and displayed using `cv2.imshow()`.
5. **Key Controls** –

   * `esc`: exits the loop and closes all windows

---

## Parameters

You can tweak these parameters inside `detectMultiScale()` to fine-tune performance:

```python
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)
```

* `scaleFactor`: How much the image size is reduced at each image scale (lower = more accurate but slower)
* `minNeighbors`: How many neighbors each rectangle should have to be retained (higher = fewer detections)

---

## Output

* **Window Preview**: Real-time video stream with bounding boxes and total number of detected faces.
