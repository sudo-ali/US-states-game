import turtle
import pandas
screen = turtle.Screen()
screen.title("General")
image = '100_Days/projects/day-25-us-states-game-start/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("100_Days/projects/day-25-us-states-game-start/50_states.csv")
data_dict = data.to_dict()
states = data['state']
states_list = states.to_list()
xcor = data['x']
xcor_list = xcor.to_list()
ycor = data['y']
ycor_list = ycor.to_list()
def write(ans, x, y):
    pass
game_is_on = True
score = 0
answer_state = screen.textinput("Guess the State", "What's another name?")
states_lower = []
for i in states_list:
    state = map(lambda x:x.lower(), states_list)
    states_list = list(state)
guesses = []
while game_is_on:
    for state in states_list:
        if answer_state == 'exit':
            game_is_on = False
        if answer_state.lower() == state.lower():
            score += 1
            state_column = data[data.state == f'{answer_state.lower()}']
            state_index = states_list.index(f'{answer_state.lower()}')
            x = xcor_list[state_index]
            y = ycor_list[state_index]
            state_y = state_column.y
            pen = turtle.Turtle()
            pen.hideturtle()
            pen.penup()
            pen.goto(x, y)
            pen.write(f"{answer_state}", move=False, align="center", font= ("Courier", 15, "normal"))
            guesses.append(answer_state)
    answer_state = screen.textinput(f"Current score: {score}", "What's another name?")
    if score == 50:
        game_is_on = False
toBeLearned = []
# for state in states_list:
#     if state not in guesses:
#         toBeLearned.append(state)
new = [toBeLearned.append(state) for state in states_list if state not in guesses]
print(toBeLearned)
data = pandas.DataFrame(toBeLearned)
data.to_csv("100_Days/projects/day-25-us-states-game-start/tobelearned.csv")
screen.exitonclick()