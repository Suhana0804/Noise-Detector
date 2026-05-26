import sounddevice as sd
import numpy as np
import tkinter as tk
from tkinter import messagebox
import time
import csv
import threading
import cv2

THRESHOLD=10
DURATION=1
CSV_LOG="noise_log.csv"

with open (CSV_LOG,"w", newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Time","Volume(db)"])

a=tk.Tk()
a.geometry("400x400")
a.title("Noise Detector")
a.configure(bg="light blue")
b=tk.Label(a,text="Status:monitoring",fg="green",bg="white",width=30,height=2,font=("Times New Roman",24))
c=tk.Label(a,text="Volume:0db",fg="red",bg="yellow",width=30,height=2,font=("Times New Roman",24))
d=tk.Label(a,text="",fg="orange",bg="light green",width=30,height=2,font=("Times New Roman",24))
b.pack()
c.pack()
d.pack()

def get_volume(indata):
    volume_norm=np.linalg.norm(indata)*10
    return int(volume_norm)

def log_noise(volume):
    with open (CSV_LOG, "a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([time.strftime("%H:%M:%S"),volume])

def capture_face_image():
    cap=cv2.VideoCapture(0)
    ret,frame=cap.read()
    if ret:
        timestamp=time.strftime("%H%M%S")
        filename=f"face_{timestamp}.jpg"
        cv2.imwrite(filename,frame)
    cap.release()
def alert_user(volume):
    b.config(text="status:noise detected",fg="red")
    d.config(text=f"noise level:{volume} db")
    a.update()
    capture_face_image()

def reset_gui():
    b.config(text="status:monitoring", fg="black")
    d.config(text="")
    a.update()
def audio_callback(indata,frames,time_info,status):
    volume=get_volume(indata)
    c.config(text=f"volume:{volume} db")
    if volume > THRESHOLD:
        log_noise(volume)
        alert_user(volume)
        time.sleep(1.5)
        reset_gui()
def start_monitoring():
    with sd.InputStream(callback=audio_callback):
        while True:
            time.sleep(DURATION)
def run_monitoring():
    monitor_thread=threading.Thread(target=start_monitoring)
    monitor_thread.daemon=True
    monitor_thread.start()
run_monitoring()
a.mainloop()