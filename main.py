from tkinter import *
import pandas
from random import choice

# ------------------------Read Csv---------------------
words = pandas.read_csv("data/words.csv")
words_dict = words.to_dict(orient="records")
display_word = choice(words_dict)

# -------------------------------UI-----------------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flash_canvas = Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_image = PhotoImage(file="images/card_front.png")
flash_canvas.create_image(400, 263, image=flash_image)
flash_canvas.create_text(400, 150, text="Title", font=("Arial", 30, "italic"))
flash_canvas.create_text(400, 250, text="Word", font=("Arial", 50, "bold"))
flash_canvas.grid(row=0, column=0, columnspan=2)

right_canvas = Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
right_image = PhotoImage(file="images/right.png")
right_canvas.create_image(50, 50, image=right_image)
right_canvas.grid(row=1, column=1)

wrong_canvas = Canvas(width=100, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_canvas.create_image(50, 50, image=wrong_image)
wrong_canvas.grid(row=1, column=0)
window.mainloop()
