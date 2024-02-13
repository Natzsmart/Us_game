#Working with Pandas and Turtle

import turtle
import pandas
screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y): 
    # This function gives us the location of x and y on the map.
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()

data = pandas.read_csv('50_states.csv')


answer_state = turtle.textinput(title='Guess the state', prompt="What's another state name?")
print(answer_state)

# Problems to solve 
#1. Convert the guess to Title case
#2. Check if the guess is among 50 states 
#3. Write correct guesses onto the map
#4. Use loop to allow user to keep guessing 
#5. Record the correct guesses 
#6. Keep track of the score