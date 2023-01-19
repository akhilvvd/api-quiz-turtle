from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = Label()
        self.score.config(text="Score:0", fg="white", bg=THEME_COLOR, highlightcolor="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 125, width=280, text="hi", font=("Arial", 20, "italic"), fill="black")
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.button = Button()
        self.button.config(image=true_image, borderwidth=0, command=self.true_answer)
        self.button.grid(row=2, column=0)

        self.button1 = Button()
        self.button1.config(image=false_image, borderwidth=0, command=self.false_answer)
        self.button1.grid(row=2, column=1)

        self.next_question_get()

        self.window.mainloop()

    def next_question_get(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You've reached the end of the questions")
            self.button1.config(state="disabled")
            self.button.config(state="disabled")


    def true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))
    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer=self.button1)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question_get)


