import pandas
import turtle
screen = turtle.Screen()
screen.title("India States Game")
image = "India.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(1000,850)
data = pandas.read_csv("india_s.csv")
all_states = data.States.to_list()
guessed_states = []

while len(guessed_states) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/30 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
       break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.States == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

screen.mainloop()