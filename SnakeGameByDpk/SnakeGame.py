import turtle
import random
import time

bodies = []
delay = 0.1
sc = 0
hs = 0
is_paused = False

# Create screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")
s.setup(width=600, height=600)

# Create head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Create food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.fillcolor("blue")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# Create scoreboard
sb = turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-250, 250)
sb.write("Score: 0  | Highest Score: 0", align="left", font=("Arial", 14, "normal"))

# Functions for moving in all directions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def togglePause():
    global is_paused
    is_paused = not is_paused

def move():
    if is_paused or head.direction == "stop":
        return
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(togglePause, "p")
s.onkey(lambda: s.bye(), "q")

# Main game loop
while True:
    s.update()  # Update the screen
    move()

    # Check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        # Hide bodies
        for body in bodies:
            body.goto(1000, 1000)  # Move bodies off-screen
        bodies.clear()
        sc = 0
        delay = 0.1
        sb.clear()
        sb.write("Score: 0  | Highest Score: {}".format(hs), align="left", font=("Arial", 14, "normal"))

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Increase the body of the snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  # Append the new body in the list

        # Increase score and update scoreboard
        sc += 10  # Increase the score by 10
        delay -= 0.001  # Decrease delay to increase speed

        if sc > hs:
            hs = sc  # Update highest score

        sb.clear()
        sb.write("Score: {}  | Highest Score: {}".format(sc, hs), align="left", font=("Arial", 14, "normal"))

    # Move snake bodies
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    # Check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            # Hide bodies
            for body in bodies:
                body.goto(1000, 1000)  # Move bodies off-screen
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: 0  | Highest Score: {}".format(hs), align="left", font=("Arial", 14, "normal"))

    time.sleep(delay)
s.mainloop()
