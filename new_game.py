import turtle
import pandas

screen = turtle.Screen()
screen.title('New game')
image= 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states=data.state.to_list()
guessed_state =[]

while len(guessed_state)<50:
    answer_states =screen.textinput(title=f'{len(guessed_state)}/50 Correct States', prompt="What's the next state?").title()
    # print(answer_states)

    if answer_states == 'Exit':
            #Using Python list comprehension break this lines of code into a single list.
        missing_states = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('magic.csv')
        break

    if answer_states in all_states:
        guessed_state.append(answer_states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_states]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(answer_states)

#urtle.exitonclick()