# Constants
BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
# TODO 1. Importing modules
from tkinter import *
import pandas
import random

# Read the CSV data file
# try open the words_to_learn file if exists (it's not at the begging of the program)
try:
    words_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_file = pandas.read_csv("./data/french_words.csv")

random_fr_card = {}

# ----------------------- GENERATE WORDS ----------------------- #
def gen_fr_words():
    global random_fr_card, flip_timer
    window.after_cancel(flip_timer)
    random_fr_card = random.choice(words)
    front_card.itemconfig(front_img, image=front_card_img)
    front_card.itemconfig(lang_text, text="French", fill="black")
    front_card.itemconfig(word_text, text=random_fr_card["French"], fill="black")
    flip_timer = window.after(4000, get_en_words)

def is_known():

    words.remove(random_fr_card)
    df = pandas.DataFrame(words)
    df.to_csv("./data/words_to_learn.csv", index=False)
    gen_fr_words()

def get_en_words():
    random_en = random_fr_card["English"]
    front_card.itemconfig(front_img, image=back_card_img)
    front_card.itemconfig(lang_text, text="English", fill="white")
    front_card.itemconfig(word_text, text=random_en, fill="white")


words = words_file.to_dict(orient="records")

# TODO 2. Setup the APP UI
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=gen_fr_words)

# TODO 3. Setup the buttons/labels
# creating the cards
front_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./Images/card_back.png")
front_img = front_card.create_image(400, 270, image=front_card_img)
lang_text = front_card.create_text(400, 150, text="language", font=("Arial", 40, "italic"))
word_text = front_card.create_text(400, 262, text="word", font=("Arial", 60, "bold"))

front_card.grid(column=0, row=0, columnspan=2)


# creating buttons
yes_image = PhotoImage(file="./images/right.png")
no_image = PhotoImage(file="./images/wrong.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=is_known)
no_button = Button(image=no_image, highlightthickness=0, command=gen_fr_words)

yes_button.grid(column=1, row=1)
no_button.grid(column=0, row=1)

gen_fr_words()

window.mainloop()


