# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle
import math
import time
import random


def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(
		    f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")


def set_image(sprite, image_filename):
    image_file = f"./Images/{image_filename}.gif"
    screen = turtle.Screen()
    screen.register_shape(image_file)
    sprite.shape(image_file)


def create_sprite(image_filename, x=0, y=0):
    sprite = turtle.Turtle()
    set_image(sprite, image_filename)
    sprite.penup()
    sprite.goto(x, y)
    window.update()
    return sprite


def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)


def draw_rectangle(color="black", x=0, y=0, width=100, height=100,):
	sprite = turtle.Turtle()
	sprite.speed(0)
	sprite.pencolor(color)
	sprite.color(color)
	sprite.penup()
	sprite.goto(x - (width*0.5), y + (height*0.5))
	sprite.pendown()
	sprite.begin_fill()
	for i in range(2):
		sprite.forward(width)
		sprite.right(90)
		sprite.forward(height)
		sprite.right(90)
	sprite.end_fill()
	sprite.hideturtle()


window = turtle.Screen()
window.tracer(0)


# Section 2: Setup
# TODO - create your player character soccer ball
s1 = create_sprite("soccerball",0,0)

# TODO - create some other sprite. maybe a goal or a person or just a shape, idc
s2 = create_sprite("goal",0,200)


# Section 3: Controls
# TODO - copy and paste all of the section 3 code from intro_movement.py
def move_up():
    s1.setheading(90)
    s1.forward(1)


def move_down():
    s1.setheading(270)
    s1.forward(1)


def move_left():
    s1.setheading(180)
    s1.forward(1)


def move_right():
    s1.setheading(0)
    s1.forward(1)


window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1
 	# TODO
    # write an if statement using get_distance(s1,s2) < 20
	# you will need to test if 20 is the right number for them touching
	# an if statment looks like
	# if ________________:
	#      break
	if get_distance (s1,s2) < 20:
		break




	window.update()


print("Game Over")