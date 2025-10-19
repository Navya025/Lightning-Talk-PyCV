# Face & Eye Detection using OpenCV

This project uses **OpenCV’s Haar Cascade Classifiers** to perform **real-time face and eye detection** via your webcam. It also allows you to **capture snapshots** of the video feed.

---

## Features

* Real-time **face and eye detection** using Haar cascades
* Automatically opens your **default webcam** (`VideoCapture(0)`)
* **Draws bounding boxes** around detected faces and eyes
* **Press `c`** to capture and save a snapshot
* **Press `q`** to exit the window safely

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
2. Save the script as `face_eye_webcam.py`.
3. Run it using:

   ```bash
   python face_eye_webcam.py
   ```
4. A window will open showing the webcam feed.

   * Press **`c`** to save a snapshot (`captured_image.jpg`)
   * Press **`q`** to quit the program

---

## Code Overview

```python
import cv2

# Load pre-trained Haar cascades for face and eye detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)
```

1. **Cascade Loading** – Loads the Haar cascade XML files that contain pre-trained models for detecting faces and eyes.
2. **Video Stream** – Opens your webcam using `cv2.VideoCapture(0)`.
3. **Frame Loop** – Continuously reads frames, converts them to grayscale, and runs `detectMultiScale()` to find faces and eyes.
4. **Drawing & Display** – Rectangles are drawn around detected regions and displayed using `cv2.imshow()`.
5. **Key Controls** –

   * `c`: saves the frame as `captured_image.jpg`
   * `q`: exits the loop and closes all windows

---

## Parameters

You can tweak these parameters inside `detectMultiScale()` to fine-tune performance:

```python
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
```

* `scaleFactor`: How much the image size is reduced at each image scale (lower = more accurate but slower)
* `minNeighbors`: How many neighbors each rectangle should have to be retained (higher = fewer detections)

---

## Output

* **Window Preview**: Real-time video stream with bounding boxes.
* **Snapshot**: Saved as `captured_image.jpg` in your working directory when pressing **`c`**.

