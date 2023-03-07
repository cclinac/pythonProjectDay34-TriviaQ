import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = tk.Label(text=f"Score: {self.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        self.main_canvas = tk.Canvas(height=250, width=300, bg="white", highlightthickness=0)
        self.question_text = self.main_canvas.create_text(
            150,
            125,
            text="",
            width=280,
            font=("Ariel", 20, "italic"),
            fill=THEME_COLOR
            )
        self.right_button_image = tk.PhotoImage(file="./images/true.png")
        self.right_button = tk.Button(image=self.right_button_image, highlightthickness=0, command=self.clicked_true)
        self.wrong_button_image = tk.PhotoImage(file="./images/false.png")
        self.wrong_button = tk.Button(image=self.wrong_button_image, highlightthickness=0, command=self.clicked_false)
        self.main_canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.main_canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.main_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.main_canvas.itemconfig(self.question_text, text="End of the quiz.")
            self.wrong_button.config(state="disable")
            self.right_button.config(state="disable")
    def clicked_true(self):
        is_correct = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_correct)

    def clicked_false(self):
        is_correct = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_correct)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.main_canvas.config(bg="green")
        else:
            self.main_canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
