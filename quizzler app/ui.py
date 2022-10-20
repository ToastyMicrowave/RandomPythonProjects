from tkinter import Button, Canvas, Label, Tk, PhotoImage

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain) -> None:
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(
            text="Score: 0/0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150, 125, text="", font=("Arial", 20, "italic"), width=280, fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2)

        self.get_next_question()

        true_button_img = PhotoImage(
            file=r"C:\Python Projects\quizzler app\images\true.png")
        false_button_img = PhotoImage(
            file=r"C:\Python Projects\quizzler app\images\false.png")

        self.true_button = Button(
            image=true_button_img, highlightthickness=0, command=self.true_pressed)

        self.false_button = Button(
            image=false_button_img, highlightthickness=0, command=self.false_pressed)

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(
                self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def update_score(self):
        self.score_label.config(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.update_score()
        self.window.after(1000, self.get_next_question)
