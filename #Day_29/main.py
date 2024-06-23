from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    pass_field.delete(0, END)
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(choice(letters))

    for char in range(nr_symbols):
        password_list += choice(symbols)

    for char in range(nr_numbers):
        password_list += choice(numbers)

    shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_field.insert(index=0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_user():
    user = user_info_field.get()
    password = pass_field.get()
    website = website_field.get().title()
    saved_data = f"{website} | {user} | {password}\n"

    if not user or not password or not website:
        messagebox.showinfo(title="Error", message="Don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {user}\nPass: {password}\n")
        if is_ok:
            user_info_field.delete(0, END)
            pass_field.delete(0, END)
            website_field.delete(0, END)
            with open("data.txt", "a") as data_file:
                data_file.write(saved_data)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(column=1, row=0)

# Creating the labels
website_label = Label(text="Website:")
user_info = Label(text="Email/Username:")
pass_label = Label(text="Password:")

website_label.grid(column=0, row=1)
user_info.grid(column=0, row=2)
pass_label.grid(column=0, row=3)

# Create Entries
website_field = Entry(width=30)
user_info_field = Entry(width=30)
pass_field = Entry(width=25)
user_info_field.insert(0, "ahmedosama@gmail.com")

website_field.focus()
website_field.grid(column=1, row=1, columnspan=2)
user_info_field.grid(column=1, row=2, columnspan=2)
pass_field.grid(column=1, row=3)

# Create buttons
generate_password_button = Button(text="Generate Password", command=generate_pass)
add_button = Button(text="Add", width=36, command=add_user)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
