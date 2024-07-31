import turtle
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.tracer(0)
turtle.bgpic(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

us_states_data = pandas.read_csv("50_states.csv")
states = us_states_data["state"]
states_guessed = []


def display_state_name(rowData):
    state_name = rowData.state.values[0]
    x_cor = rowData.x.values[0]
    y_cor = rowData.y.values[0]
    pen.setpos(x_cor, y_cor)
    pen.write(state_name, False, "center")
    states_guessed.append(state_name)


def get_state_data(guess):
    target_row_data = us_states_data[us_states_data["state"] == guess]
    if not target_row_data.empty and states_guessed.count(guess) < 1:
        return target_row_data


def start_game():
    while True:
        user_guess = screen.textinput(title=f"{len(states_guessed)}/50 States Correct",
                                        prompt="Type the name of a state")
        state_guess_data = get_state_data(user_guess.title())
        if not state_guess_data.empty:
            display_state_name(state_guess_data)
        screen.update()


start_game()


def get_mouse_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_coor)
turtle.mainloop()
