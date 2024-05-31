# coding=utf-8
# @rizzyneck

from datetime import datetime, timedelta
import tkinter as tk, zlib, base64,os
from tkinter import messagebox


class Timer:
    def __init__(self, days: float = 0, minutes: float = 0, seconds: float = 0, filename: str = "end_time.txt", locked=True):
        self.days = days
        self.minutes = minutes
        self.seconds = seconds
        self.time_finish = datetime.now() + timedelta(days=self.days, minutes=self.minutes, seconds=self.seconds)
        self.filename = filename
        self.locked = locked
        
    def save_end_time(self):
        if not self.locked:
            if os.path.isfile(self.filename):
                with open(self.filename, 'w') as file:
                    time_str = self.time_finish.isoformat()
                    file.write(base64.b64encode(zlib.compress(f'{time_str}'.encode())).decode())
                    return
            
    def load_end_time(self):
        with open(self.filename, 'r') as file:
            time_str = file.read().strip()
            self.time_finish = datetime.fromisoformat(zlib.decompress(base64.b64decode(time_str)).decode())

    def check_end_time(self):
        if self.time_finish and datetime.now() >= self.time_finish:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            messagebox.showerror(
                "Login Error!!",
                message="First activate the user and come back to log in again!"
            )
            root.destroy()  # Destroy the root window after the message box is closed


# Create a timer instance with the desired duration
timer = Timer(seconds=50, locked=False)
timer.save_end_time()
timer.load_end_time()
timer.check_end_time()
