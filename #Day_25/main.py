import turtle as tr

import pandas
import pandas as pd
# Turtle module work with gif image format only
image = "blank_states_img.gif"
states_df = pd.read_csv("50_states.csv")

# TODO 1. setup the screen
screen = tr.Screen()
screen.title("U.S Game")
screen.addshape(image)
tr.shape(image)

score = 0
correct_states = 0
guessed_states = []

# TODO 2. capture the (x,y) axis of the states , then capture the states names
states_list = states_df["state"].to_list()  # convert it int0 list to make the search process easier


while correct_states < 50:
    answer_state = screen.textinput(title=f"Guess a State {correct_states}/50", prompt="Enter a State").title()

    if answer_state == "Exit":
      break

    elif answer_state in states_list:
        correct_states += 1
        new_state = tr.Turtle()
        get_pos = states_df[states_df.state == answer_state]
        x_pos = get_pos.x.iloc[0]
        y_pos = get_pos.y.iloc[0]
        new_state.penup()
        new_state.hideturtle()
        new_state.goto(x_pos, y_pos)
        new_state.write(answer_state, align="center", font=('Arial', 8, 'normal'))

        states_list.remove(answer_state)

# States to learn (includes the remaining states that you didn't guess it
remaining_states = pandas.Series(states_list)
remaining_states.to_csv("remaining_states.csv")


screen.exitonclick()
# You can use turtle module to know the (x,y) coordinates from the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# tr.onscreenclick(get_mouse_click_coor)
# tr.mainloop()