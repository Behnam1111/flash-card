from tkinter import *
import pandas
from random import choice

# ------------------------Read Csv---------------------
words = pandas.read_csv("data/words.csv")
words_dict = words.to_dict(orient="records")
display = choice(words_dict)["English"]


# ------------------------Display word--------------------
def display_word():
    global display
    global word_text
    display = choice(words_dict)["English"]
    flash_canvas.delete(word_text)
    word_text = flash_canvas.create_text(400, 250, text=display, font=("Arial", 50, "bold"))

    print(display)


# -------------------------------UI-----------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flash_canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_image = PhotoImage(file="images/card_front.png")
flash_canvas.create_image(400, 263, image=flash_image)

title_text = flash_canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
word_text = flash_canvas.create_text(400, 250, text=display, font=("Arial", 50, "bold"))
flash_canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(command=display_word, image=wrong_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(command=display_word, image=right_image, borderwidth=0, highlightthickness=0, bg=BACKGROUND_COLOR)
right_button.grid(row=1, column=1)
window.mainloop()
