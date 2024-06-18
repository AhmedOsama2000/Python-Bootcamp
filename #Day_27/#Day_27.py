"""
TKinter (Python interface to TCL/TK) Module: used to create GUI Apps
- it's wrapper functions for TCL/TK
- More about python arguments:
==> for default argument:
    - def fun(a=1,b=2,c=3): (now you don't have to provide any argument
==> *args (many positional arguments):
    - def fun(*args): (now you can add any number of any arguments, it will be a form of tuple)
    - so it can be indexed
==> *kwargs (many keyword arguments):
    - def fun(**kwargs): (kwargs is type of dictionary)
    - it allows passing keywords with their corresponding values
    - kwargs with classes:
    class Car():
        def __init__(self, **kwargs):
            self.make = kwargs.get("make)
            self.model = kwargs.get("model") (won't through an error when not
            passing any of the attributes to the class when taking an instance)
"""
# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# # craeting labels
# my_label = Label(text="I'm a label", font=("Arial", 20, "bold"))
#
# my_label["text"] = "My new label"
# my_label.config(text="new text")
# my_label.pack()
#
#
# def click_button():
#     my_label.config(text=input_text.get())
#
# # creating buttons
# button = Button(text="Click Me", command=click_button)
# button.pack()
#
# # Entry component
# input_text = Entry(window, width=10)
# input_text.pack()

# Adding text entry box, spinbox, radio buttons ...
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()




# # keep the screen open
# window.mainloop()
