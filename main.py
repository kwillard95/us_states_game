import turtle
import pandas
import time



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
remaining_states = us_states_data.state.to_list()


def display_remaining_states():
    x_cor = 0
    y_cor = 300
    pen.setpos(x_cor, y_cor)
    pen.write("Here are the states you missed:", False, "center", ("Arial", 24, "normal"))
    for index in range(0, len(remaining_states)):
        if index < 25:
            x_cor = -180
        elif index == 25:
            x_cor = 100
            y_cor = 300
        y_cor -= 20
        pen.setpos(x_cor, y_cor)
        pen.write(remaining_states[index], False, "left", ("Arial", 18, "normal"))


def display_state_name(rowData):
    state_name = rowData.state.values[0]
    x_cor = rowData.x.values[0]
    y_cor = rowData.y.values[0]
    pen.setpos(x_cor, y_cor)
    pen.write(state_name, False, "center")
    remaining_states.remove(state_name)
    # states_guessed.append(state_name)


def get_state_data(guess):
    target_row_data = us_states_data[us_states_data["state"] == guess]
    if not target_row_data.empty and remaining_states.count(guess) > 0:
        return target_row_data


def start_game():
    game_running = True
    while game_running:
        user_guess = screen.textinput(title=f"{50 - len(remaining_states)}/50 States Correct",
                                        prompt=f"Type the name of a state.")
        print(user_guess)
        if user_guess is not None:
            state_guess_data = get_state_data(user_guess.title())
            if state_guess_data is not None:
                display_state_name(state_guess_data)
            if len(remaining_states) < 1:
                game_running = False
                pen.setpos(0,0)
                pen.write("Congrats! You guessed all 50 states!", False, "center", ("Arial", 38, "normal"))
        elif user_guess is None:
            game_running = False
            display_remaining_states()

        screen.update()


start_game()


def get_mouse_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_coor)
turtle.mainloop()
