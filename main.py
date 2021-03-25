import turtle
import pandas

screen = turtle.Screen()
screen.screensize(700, 600)
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

states_correct = 0

guessed_states = []


while states_correct != 50:
    answer_state = screen.textinput(f"{states_correct}/50 States Correct", "What's the name of the state?").title()
    states_name = states["state"].to_list()

    if answer_state in states_name:
        states_correct += 1
        state = states[states["state"] == answer_state]
        x = int(state["x"])
        y = int(state["y"])
        state_written = turtle.Turtle()
        state_written.penup()
        state_written.hideturtle()
        state_written.goto(x, y)
        state_written.write(answer_state, "center", font=("Arial", 12, "normal"))
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        break

states_to_learn = []

for state in states["state"]:
    if state not in guessed_states:
        states_to_learn.append(state)

states_tl_dict = {
    "state": [*states_to_learn]
}

print(states_tl_dict)

state_tl = pandas.DataFrame(states_tl_dict)
state_tl.to_csv("states_to_learn.csv")





        
     

    


turtle.mainloop()



