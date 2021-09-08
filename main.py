from tkinter import *
import pandas
import random

current_word = {}
words_dict = {}
BACKGROUND_COLOR = "#B1DDC6"
# ------------------------Read Csv---------------------
try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_data = pandas.read_csv("data/french_words.csv")
    words_dict = french_data.to_dict(orient="records")
else:
    words_dict = words.to_dict(orient="records")



# ------------------------Display word--------------------
def display_word():
    global current_word
    global flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_dict)
    flash_canvas.itemconfig(title_text, text="French", fill="black")
    flash_canvas.itemconfig(word_text, text=current_word["French"], fill="black")
    flash_canvas.itemconfig(flash_canvas_image, image=flash_image_front)
    flip_timer = window.after(3000, func=flip_card)


# ----------------------------Flip Card-----------------------------
def flip_card():
    flash_canvas.itemconfig(flash_canvas_image, image=flash_image_back)
    flash_canvas.itemconfig(title_text, text="English", fill="white")
    flash_canvas.itemconfig(word_text, text=current_word["English"], fill="white")


# -----------------------------Remove Card-----------------------------
def remove_card():
    words_dict.remove(current_word)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    display_word()

# -------------------------------UI-----------------------------


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

flash_canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_image_front = PhotoImage(file="images/card_front.png")
flash_image_back = PhotoImage(file="images/card_back.png")
flash_canvas_image = flash_canvas.create_image(400, 263, image=flash_image_front)
title_text = flash_canvas.create_text(400, 150, text="", font=("Arial", 30, "italic"))
word_text = flash_canvas.create_text(400, 250, text="", font=("Arial", 50, "bold"))
flash_canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=display_word, image=wrong_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(command=remove_card, image=right_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)
display_word()
window.mainloop()
