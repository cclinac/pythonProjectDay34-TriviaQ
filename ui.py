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
        q_text = self.quiz.next_question()
        self.main_canvas.itemconfig(self.question_text, text=q_text)

    def clicked_true(self):
        self.score = self.quiz.check_answer(user_answer="True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()

    def clicked_false(self):
        self.score = self.quiz.check_answer(user_answer="False")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.get_next_question()
