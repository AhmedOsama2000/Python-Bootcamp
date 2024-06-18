from tkinter import *
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=300,height=100)
window.config(padx=40,pady=30)

# TODO 1. Add the labels
# assuming it's 3x3 grid
miles = Label(text="Miles",font=(12))
is_equal_to = Label(text="is equal to",font=(12))
km = Label(text="Km",font=(12))

my_label = Label()
def convert_to_km():
    distance = entry.get()
    my_label.config(text=float(distance)*(1.609344))
    my_label.grid(column=1,row=2)

km.grid(column=2,row=2)
miles.grid(column=2,row=0)
is_equal_to.grid(column=0,row=2)

# TODO 2. create button
calculate = Button(text="Calculate",command=convert_to_km)
calculate.config(font=(12))
calculate.grid(column=1,row=3)


# TODO 3. create the entry
entry = Entry(width=12)
entry.grid(column=1,row=0)


window.mainloop()