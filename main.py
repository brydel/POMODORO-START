import tkinter as tk
from tkinter import Canvas, Label, Button, PhotoImage
import math

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.reps = 0
        self.timer = None

        self.root.title("Pomodoro Timer")
        self.root.config(padx=100, pady=50, bg=YELLOW)

        self.title_label = Label(root, text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
        self.title_label.grid(column=1, row=0)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.canvas.grid(column=1, row=1)
        self.timer_text = self.canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

        self.start_button = Button(root, text="Start", command=self.start_timer, highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        self.start_button.grid(column=0, row=2)

        self.reset_button = Button(root, text="Reset", command=self.reset_timer, highlightthickness=0, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        self.reset_button.grid(column=2, row=2)

        self.check_mark = Label(root, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
        self.check_mark.grid(column=1, row=3)

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.title_label.config(text="Timer", fg=YELLOW)
        self.check_mark.config(text="")
        self.reps = 0

    def start_timer(self):
        self.reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        
        if self.reps % 8 == 0:
            self.countdown(long_break_sec)
            self.title_label.config(text="Long Break", fg=RED)
        elif self.reps % 2 == 0:
            self.countdown(short_break_sec)
            self.title_label.config(text="Short Break", fg=PINK)
        else:
            self.countdown(work_sec)
            self.title_label.config(text="Work", fg=GREEN)

    def countdown(self, count):
        count_min = count // 60
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.canvas.itemconfig(self.timer_text, text=f"{count_min}:{count_sec}")
        if count > 0:
            self.timer = self.root.after(1000, self.countdown, count - 1)
        else:
            self.start_timer()
            marks = "✔" * (math.floor(self.reps / 2))
            self.check_mark.config(text=marks)

# Driver Code
if __name__ == "__main__":
    root = tk.Tk()
    pomodoro_app = PomodoroTimer(root)
    root.mainloop()
