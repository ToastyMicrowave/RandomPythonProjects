from tkinter import Tk, PhotoImage, Canvas, Button
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

change_trigger = None


# WORD MANAGEMENT
try:
    data = pandas.read_csv(
        r"C:\Python Projects\Flash Card app\data\Words To Learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pandas.read_csv(
        r"C:\Python Projects\Flash Card app\data\french_words.csv").to_dict(orient="records")


def did_know():
    data.remove(random_word)
    pandas.DataFrame(data).to_csv(
        path_or_buf="./data/Words To Learn.csv", index=False, columns=["French", "English"])
    get_french_word()


def did_not_know():
    get_french_word()


def get_french_word():
    global change_trigger
    global random_word
    if change_trigger is not None:
        window.after_cancel(change_trigger)
    random_word = random.choice(data)
    canvas.itemconfig(card_img, image=CARD_FRONT_IMG)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=random_word["French"], fill="black")
    change_trigger = window.after(
        3000, change_to_translation)


def change_to_translation():
    canvas.itemconfig(card_img, image=CARD_BACK_IMG)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=random_word["English"], fill="white")


# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

CARD_FRONT_IMG = PhotoImage(
    file=r"C:\Python Projects\Flash Card app\images\card_front.png")
CARD_BACK_IMG = PhotoImage(
    file=r"C:\Python Projects\Flash Card app\images\card_back.png")
RIGHT_IMG = PhotoImage(
    file=r"C:\Python Projects\Flash Card app\images\right.png")
WRONG_IMG = PhotoImage(
    file=r"C:\Python Projects\Flash Card app\images\wrong.png")

canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0,
                width=800, height=526)
card_img = canvas.create_image(400, 263, image=CARD_FRONT_IMG)
language_text = canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = Button(command=did_not_know, image=WRONG_IMG,
                      highlightthickness=0, border=0)
right_button = Button(command=did_know, image=RIGHT_IMG,
                      highlightthickness=0, border=0)
wrong_button.grid(column=0, row=1)
right_button.grid(column=1, row=1)

get_french_word()

window.mainloop()
