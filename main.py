#!/usr/bin/python3

import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
screen.setup(width=618, height=645)
image = "blank_india_state.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("states.csv")
no_of_states = len(data)

user_ans_list = []
no_of_correct_ans = 0

missing_ans_dict = {"Missing States": []}
df = pandas.DataFrame(missing_ans_dict)
df.to_csv("states_to_learn.csv")

while len(user_ans_list) < no_of_states:
    user_ans = screen.textinput(title=f"Guess the State {no_of_correct_ans}/{no_of_states}", prompt="What's another State's name? ").title()

    if(user_ans == "Exit"):
        missing_ans = []
        for x in data["state"].to_list():
            if(x not in user_ans_list):
                missing_ans.append(x)
        missing_ans_dict = {"Missing States": missing_ans}
        df = pandas.DataFrame(missing_ans_dict)
        df.to_csv("states_to_learn.csv")
        break

    if(user_ans in data["state"].to_list() and user_ans not in user_ans_list):
        user_ans_list.append(user_ans)
        data_of_state = data[data["state"] == user_ans]
        x = int(data_of_state["x"])  
        y = int(data_of_state["y"])
        
        mark = turtle.Turtle()
        mark.hideturtle()
        mark.penup()
        mark.goto(x,y)
        mark.write(f"{user_ans}", align="center")
        # mark.write(f"{data_of_state.state.item()}", align="center")
        no_of_correct_ans += 1
