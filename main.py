import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


def main():
    game_over = False
    correct = 0
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()

    # The below processes were used for determining the coordinates for the state names:
    # turtle.onscreenclick(get_click_coor)
    # turtle.mainloop()

    state_table = pandas.read_csv("50_states.csv")
    state_list = state_table.state.to_list()

    while not game_over:
        if correct == 0:
            answer = screen.textinput(title="Guess the State", prompt="Name a state: ").title()
        else:
            answer = screen.textinput(title=f"{correct}/50 correct", prompt="Name a state: ").title()
        if answer in state_list:
            # This is my original code. The other bit of code that also does this is the alternate I found.
            # x = state_table[state_table.state == answer].x.values[0]
            # y = state_table[state_table.state == answer].y.values[0]
            # writer.goto(x, y)
            state_data = state_table[state_table.state == answer]
            writer.goto(int(state_data.x), int(state_data.y))
            writer.write(answer)
            correct += 1
            state_list.remove(answer)
        elif answer == "":
            game_over = True
            print(state_list)
        if correct == 50:
            writer.goto(0, 175)
            writer.write("You aced it! Good job!")
            game_over = True
            screen.exitonclick()
    writer.write(f"You got {correct} states.")
    df = pandas.DataFrame(state_list)
    df.to_csv("states_missed.csv")
    screen.exitonclick()


# This function was used with the commented out section in main() to obtain state name coordinates.
# def get_click_coor(x, y):
#     print(x, y)

if __name__ == '__main__':
    main()
