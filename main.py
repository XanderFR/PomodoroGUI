from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)  # Stops the timer
    # timerText  00:00
    canvas.itemconfig(timerText, text="00:00")
    # titleLabel "Timer"
    titleLabel.config(text="Timer")
    # Reset checkMarks
    checkMarks.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    reps += 1

    # Cycles in minutes => 25 work, 5 break, 25 work, 5 break, 25 work, 5 break, 25 work, 20 break
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    # If it's the 8th rep:
    if reps % 8 == 0:
        countDown(longBreakSec)
        titleLabel.config(text="Break", fg=RED)
    # If it's the 2nd, 4th, or 6th rep:
    elif reps % 2 == 0:
        countDown(shortBreakSec)
        titleLabel.config(text="Break", fg=PINK)
    # If it's the 1st, 3rd, 5th, or 7th rep:
    else:
        countDown(workSec)
        titleLabel.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    countMin = math.floor(count / 60)  # Number of minutes
    countSec = count % 60  # Number of seconds

    if countSec < 10:  # If block for the single digit displays
        countSec = f"0{countSec}"

    canvas.itemconfig(timerText, text=f"{countMin}:{countSec}")  # Changes canvas element (timerText), takes in the thing about it that you want to change, links timerText to count value and presents it in the form of a timer

    if count > 0:  # Stops the timer from becoming negative
        global timer
        timer = window.after(1000, countDown, count - 1)  # executes a command after a time delay
    else:
        startTimer()
        marks = ""  # To hold the check marks
        workSessions = math.floor(reps / 2)  # Represents the number of completed work sessions
        for _ in range(workSessions):  # For every completed work period
            marks += "✔"  # Add a check mark
        checkMarks.config(text=marks)  # Put the updated check mark sequence on the GUI

# ---------------------------- UI SETUP ------------------------------- #
# The General Window
window = Tk()
window.title("Pomodoro GUI App")
window.config(padx=100, pady=50, bg=YELLOW)

# The Timer Label
titleLabel = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
titleLabel.grid(column=1, row=0)

# The Tomato Image
canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)  # Canvas for holding images
tomatoImg = PhotoImage(file="tomato.png")  # A way to read through a file and to get hold of an image at a file location
canvas.create_image(102, 112, image=tomatoImg)  # Puts the tomato image in the canvas

# The Timer Text
timerText = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # The timer text in the middle of the tomato
canvas.grid(column=1, row=1)

# The Start Button
startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(column=0, row=2)

# The Reset Button
resetButton = Button(text="Reset", highlightthickness=0, command=resetTimer)
resetButton.grid(column=2, row=2)

# The Check Mark(s)
checkMarks = Label(fg=GREEN, bg=YELLOW)
checkMarks.grid(column=1, row=3)

window.mainloop()
