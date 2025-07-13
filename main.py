from tkinter import Tk, Label, Button, PhotoImage, Canvas
from PIL import Image, ImageTk
from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

# -------------------- Setup Questions -------------------- #
question_bank = [Question(q["question"], q["correct_answer"])
                 for q in question_data]
quiz = QuizBrain(question_bank)


# -------------------- GUI Setup -------------------- #
THEME_COLOR = "#31AAEB"

window = Tk()
window.title("Quiz Game")
window.config(padx=20, pady=20, bg=THEME_COLOR)

# Score label
score_label = Label(text="Score: 0", fg="white",
                    bg=THEME_COLOR, font=("Arial", 22))
score_label.grid(row=0, column=1, sticky="e")


canvas = Canvas(width=500, height=250,
                bg="white", highlightthickness=0)
question_text = canvas.create_text(0, 0,
                                   width=canvas.winfo_reqwidth() - 20,
                                   text="",
                                   fill="black",
                                   font=("Arial", 22, "italic"),
                                   anchor="center",
                                   tags="question"
                                   )
canvas.grid(row=1, column=0, columnspan=2, pady=20)

# Load button images and convert to PhotoImage for tkinter compatibility
true_img_raw = Image.open(
    "images/true.png").resize((240, 120), Image.Resampling.LANCZOS)
true_img = ImageTk.PhotoImage(true_img_raw)

false_img_raw = Image.open(
    "images/false.png").resize((240, 120), Image.Resampling.LANCZOS)
false_img = ImageTk.PhotoImage(false_img_raw)

# Buttons
true_button = Button(image=true_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                     activebackground=THEME_COLOR,
                     command=lambda: check_answer("True"))
true_button.grid(row=2, column=0)

false_button = Button(image=false_img, highlightthickness=0, bd=0, bg=THEME_COLOR,
                      activebackground=THEME_COLOR,
                      command=lambda: check_answer("False"))
false_button.grid(row=2, column=1)


# -------------------- Game Logic -------------------- #
def center_question_text():
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    canvas.coords("question", canvas_width / 2, canvas_height / 2)


def get_next_question():
    if quiz.still_has_questions():
        q_num = quiz.question_number + 1
        q_text = quiz.question_list[quiz.question_number].text
        canvas.itemconfig(
            question_text, text=f"Q.{q_num}: {q_text}", fill="black", font=("Arial", 22, "italic"))
    else:
        canvas.itemconfig(
            question_text, text=f"You've completed the quiz!\nFinal Score: {quiz.score}/{quiz.question_number}", fill="black", font=("Arial", 22, "italic"))
        center_question_text()
        true_button.config(state="disabled")
        false_button.config(state="disabled")


window.after(100, center_question_text)


def check_answer(user_answer):
    correct_answer = quiz.question_list[quiz.question_number].answer
    is_right = quiz.check_answer(user_answer, correct_answer)

    if is_right:
        canvas.itemconfig(question_text, text="CORRECT!",
                          fill="green", font=("Impact", 28, "bold"))
    else:
        canvas.itemconfig(question_text, text="WRONG!",
                          fill="red", font=("Impact", 28, "bold"))
    current_q_number = quiz.question_number + 1
    score_label.config(text=f"Score: {quiz.score}/{current_q_number}")

    quiz.question_number += 1
    window.after(1000, get_next_question)


# -------------------- Start -------------------- #
get_next_question()
window.mainloop()
