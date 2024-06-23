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
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Work timelines
    if reps == 1 or reps == 3 or reps == 7:
        timer_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

    # short break timelines
    elif reps == 2 or reps == 4 or reps == 6:
        timer_label.config(text="Short Break!", fg=PINK)
        count_down(short_break_sec)

    # long break timelines
    elif reps == 8:
        timer_label.config(text="Long Break!", fg=RED)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)

    else:
        reps += 1
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"

        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Program")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating labels
timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=2, row=1)

# creating buttons
start_button = Button(text="start", width=5, font=(FONT_NAME, 12, "bold"), command=start_timer)
reset_button = Button(text="reset", width=5, font=(FONT_NAME, 12, "bold"), command=reset_timer)

start_button.grid(column=1, row=5)
reset_button.grid(column=3, row=5)

# create the check mark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
check_mark.grid(column=2, row=6)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # create a canvas to allow put text/images on images layers
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # put the image in the center
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=3)

window.mainloop()