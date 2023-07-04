import time
import os

def pomodoro_timer(work_minutes, break_minutes, cycles):
    for _ in range(cycles):
        # Work session
        print("Work session started!")
        time.sleep(work_minutes * 60)  # Convert minutes to seconds
        os.system("say 'Work session ended!'")  # For macOS, use 'espeak' for Linux, or 'pyttsx3' for Windows
        
        # Break session
        print("Break session started!")
        time.sleep(break_minutes * 60)  # Convert minutes to seconds
        os.system("say 'Break session ended!'")  # For macOS, use 'espeak' for Linux, or 'pyttsx3' for Windows

# Set the duration of work session, break session, and number of cycles
work_minutes = 25
break_minutes = 5
cycles = 4

pomodoro_timer(work_minutes, break_minutes, cycles)
