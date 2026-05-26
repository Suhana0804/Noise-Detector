# Noise Detector System

This project is a real-time Noise Detection System created using Python, Tkinter, SoundDevice, NumPy, OpenCV, and CSV logging.

The application continuously monitors microphone input and detects loud sounds based on a predefined threshold value.

When the detected sound exceeds the threshold, the system:
- Detects high noise levels
- Updates the GUI status
- Logs the noise information into a CSV file
- Captures an image from the webcam automatically

The project combines audio processing, GUI development, threading, logging, and computer vision concepts.

## Features

- Real-time microphone monitoring
- Noise level calculation
- Threshold-based noise detection
- GUI status updates
- Automatic webcam image capture
- CSV logging system
- Multithreading for continuous monitoring
- Live volume display

## Technologies Used

- Python
- Tkinter
- NumPy
- SoundDevice
- OpenCV (cv2)
- CSV
- Threading

## How It Works

The program continuously listens to microphone input using SoundDevice.

The incoming audio signal is processed using NumPy to calculate sound intensity (volume level).

If the detected volume exceeds the threshold value:

1. The GUI changes status to **Noise Detected**
2. The noise level is displayed
3. The detected volume is saved into a CSV log file
4. The webcam captures an image automatically
5. The system resets and continues monitoring

## Files Generated

The program automatically creates:

- `noise_log.csv` → stores timestamp and detected noise volume
- `face_timestamp.jpg` → captured webcam images during noise events

## How to Run

Install the required libraries:

pip install sounddevice 
pip install numpy 
pip install opencv-python

Run the Python file:

python noise_detector.py

Allow microphone and webcam permissions when prompted.

## What I Learned

- Audio input processing in Python
- Real-time monitoring systems
- GUI development using Tkinter
- Working with microphone streams
- Volume calculation using NumPy
- CSV file logging
- Webcam image capture using OpenCV
- Multithreading in Python
- Combining multiple Python libraries into one application
