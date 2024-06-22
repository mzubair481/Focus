# Face Detection Mouse Control

This Python script uses OpenCV to detect faces via a webcam and moves the mouse cursor based on the face detection status. The script also uses the `screeninfo` library to determine the center positions of connected displays and moves the mouse cursor accordingly.

## Features

- Detects faces using the webcam
- Moves the mouse cursor to the center of a primary display when a face is detected
- Moves the mouse cursor to the center of a secondary display when no face is detected
- Displays a live video feed with detected faces highlighted

## Requirements

- Python 3.x
- OpenCV
- imutils
- screeninfo

## Installation

1. **Clone the repository**:

    ```sh
    https://github.com/mzubair481/Focus.git
    cd Focus
    python -m venv venv
    source venv/bin/activate
    ```

2. **Install the required packages**:

    ```sh
    pip install opencv-python imutils screeninfo
    ```

## Usage

Run the script using Python:

```sh
python main.py
