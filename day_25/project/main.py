# def get_mouse_click_coor(x,y): -----> if You to discovery mouse's coordantions
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import pandas
import turtle



#Developing screen in turtle library
screen= turtle.Screen()
screen.title("U.S. States Game")
image="day_25/project/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states=[]

while len(guessed_states)<=50:
    answer_state= screen.textinput(title= f"{len(guessed_states)}/50 ",prompt="What's another state's name? " ).title()

    #Import data
    data=pandas.read_csv("day_25/project/50_states.csv")
    all_states= data.state.to_list()
    if answer_state=="Exit":
        missing_states=[state for state in all_states if state not in guessed_states]
        # missing_states=[]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        print(missing_states)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("day_25/project/states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state ==answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(state_data.state.item( ))

screen.exitonclick()







