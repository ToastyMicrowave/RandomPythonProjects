from tkinter import Tk, Button, Label, Canvas, PhotoImage, messagebox
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_TIME = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60
CHECKMARK = "✓ "
timer = None
rep = 1

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global rep
    rep = 1
    window.after_cancel(timer)
    current_action_label["text"] = "Timer"
    current_action_label["fg"] = GREEN
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label["text"] = ""
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    if rep % 2 == 0:
        if rep == 8:
            countdown(LONG_BREAK)
            current_action_label["fg"] = RED
        else:
            countdown(SHORT_BREAK)
            current_action_label["fg"] = PINK
        messagebox.showinfo(title="Break", message="It's time to take a break!")
        current_action_label["text"] = "Break"
    else:
        current_action_label["fg"] = GREEN
        current_action_label["text"] = "Work"
        countdown(WORK_TIME)
        messagebox.showinfo(title="Work", message="It's time to get back to work!")
        
    rep += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global timer
    minutes = count // 60
    seconds = count % 60
    if seconds >= 0 and minutes >= 0:
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        timer = window.after(1000, countdown, minutes * 60 + seconds - 1)
    else:
        if rep % 2 == 0:
            checkmark_label["text"] = f"{CHECKMARK *( rep // 2)}"
        if rep == 9:
            reset_timer()
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


current_action_label = Label(text="Timer", fg=GREEN, bg=YELLOW,
                             highlightthickness=0, font=(FONT_NAME, 40, "bold"))
current_action_label.grid(column=1, row=0)

checkmark_label = Label(text="", fg=GREEN, bg=YELLOW,
                        highlightthickness=0, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)


tomato_img = PhotoImage(file=r"C:\Python Projects\Pomodoro Project\tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


reset_button = Button(command=reset_timer, text="Reset", fg=PINK, bg=YELLOW,
                      highlightthickness=0, border=0, font=(FONT_NAME, 14, "bold"))
start_button = Button(command=start_timer, text="Start", fg=PINK, bg=YELLOW,
                      highlightthickness=0, border=0, font=(FONT_NAME, 14, "bold"))
reset_button.grid(column=2, row=2)
start_button.grid(column=0, row=2)


window.mainloop()
