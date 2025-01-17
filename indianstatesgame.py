import pandas as pd
import turtle
tim = turtle.Turtle()
screen = turtle.Screen()
tim.penup()
tim.hideturtle()
screen.addshape('indian-map.gif')
turtle.shape('indian-map.gif')
data = pd.read_csv('indian_states_data.csv')
score = 0
gameon = True
correct_guesses = []

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)


while gameon:
    ans_state = screen.textinput(title=f'{score}/{len(data['States'])}', prompt='Enter a state name: ')
    for states in data['States']:
        if ans_state.lower() == states.lower():
            score += 1
            pos = data[ans_state.lower() == data['States'].str.lower()]
            xpos = int(pos.x)
            ypos = int(pos.y)
            tim.goto(x=xpos, y=ypos)
            tim.write(states)
            correct_guesses.append(states)

        if score == len(data['States'])-1:
            gameon = False
            print(f'You won')

turtle.mainloop()