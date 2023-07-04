import tkinter as tk
import time
import os

class PomodoroTimer:
    def __init__(self, work_minutes, break_minutes, cycles):
        self.work_minutes = work_minutes
        self.break_minutes = break_minutes
        self.cycles = cycles

        self.root = tk.Tk()
        self.root.title("Pomodoro Timer")

        self.label = tk.Label(self.root, text="Welcome to Pomodoro Timer", font=("Arial", 18))
        self.label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.label.config(text="Work session started!", fg="green")
        self.update_timer(self.work_minutes * 60, "Work session ended!")
        
    def update_timer(self, seconds_left, session_ended_msg):
        if seconds_left >= 0:
            minutes = seconds_left // 60
            seconds = seconds_left % 60
            timer_text = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=timer_text)
            self.root.after(1000, self.update_timer, seconds_left - 1, session_ended_msg)
        else:
            self.label.config(text=session_ended_msg, fg="red")
            os.system("say '" + session_ended_msg + "'")  # For macOS, use 'espeak' for Linux, or 'pyttsx3' for Windows
            self.cycles -= 1
            if self.cycles > 0:
                self.root.after(2000, self.start_break)
            else:
                self.start_button.config(state=tk.NORMAL)
                self.label.config(text="Welcome to Pomodoro Timer", fg="black")
                self.timer_label.config(text="")

    def start_break(self):
        self.label.config(text="Break session started!", fg="blue")
        self.update_timer(self.break_minutes * 60, "Break session ended!")

# Set the duration of work session, break session, and number of cycles
work_minutes = 25
break_minutes = 5
cycles = 4

pomodoro = PomodoroTimer(work_minutes, break_minutes, cycles)
