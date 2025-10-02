import turtle as t
import random as rd

# --- Setup ---
t.bgcolor('blue')
t.title("Caterpillar Game")

caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()

text_turtle = t.Turtle()
text_turtle.hideturtle()
text_turtle.write('Press SPACE to start', align='center', font=('Arial', 18, 'bold'))

score_turtle = t.Turtle()
score_turtle.hideturtle()

# Obstacles
num_obstacles = 5
obstacles = []
for _ in range(num_obstacles):
    obs = t.Turtle()
    obs.shape('circle')
    obs.color('red')
    obs.penup()
    obs.setposition(rd.randint(-200, 200), rd.randint(-200, 200))
    obstacles.append(obs)

# --- Game State ---
game_started = False
score = 0
caterpillar_speed = 2
caterpillar_length = 3

# --- Helpers ---
def outside_window():
    left = -t.window_width()/2
    right = t.window_width()/2
    top = t.window_height()/2
    bottom = -t.window_height()/2
    x, y = caterpillar.pos()
    return x < left or x > right or y > top or y < bottom

def display_score():
    score_turtle.clear()
    x = (t.window_width()/2) - 70
    y = (t.window_height()/2) - 70
    score_turtle.penup()
    score_turtle.setpos(x, y)
    score_turtle.write(str(score), align='right', font=('Arial', 40, 'bold'))

def place_leaf():
    leaf.hideturtle()
    leaf.setpos(rd.randint(-200,200), rd.randint(-200,200))
    leaf.showturtle()

def game_over():
    global game_started
    game_started = False
    caterpillar.hideturtle()
    leaf.hideturtle()
    t.write('GAME OVER!', align='center', font=('Arial', 30, 'bold'))

# --- Main Loop ---
def update():
    global score, caterpillar_speed, caterpillar_length

    if not game_started:
        return

    caterpillar.forward(caterpillar_speed)

    # Collision with leaf
    if caterpillar.distance(leaf) < 20:
        place_leaf()
        caterpillar_length += 1
        caterpillar.shapesize(1, caterpillar_length, 1)
        caterpillar_speed += 0.5
        score += 10
        display_score()

    # Collision with obstacles
    for obs in obstacles:
        if caterpillar.distance(obs) < 20:
            game_over()
            return

    # Outside window
    if outside_window():
        game_over()
        return

    # Schedule next frame
    t.ontimer(update, 100)

# --- Controls ---
def start_game():
    global game_started, score, caterpillar_speed, caterpillar_length
    if game_started:
        return
    game_started = True
    score = 0
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.setheading(0)
    caterpillar.goto(0,0)
    caterpillar.showturtle()
    text_turtle.clear()
    display_score()
    place_leaf()
    update()

def move_up(): caterpillar.setheading(90)
def move_down(): caterpillar.setheading(270)
def move_left(): caterpillar.setheading(180)
def move_right(): caterpillar.setheading(0)

# --- Key Bindings ---
t.listen()
t.onkey(start_game, 'space')
t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.mainloop()
