import turtle as trtl
import random
#Garnet Cheng Cameron Weiss
# named turtle light and set turtle speed as well as made the background color blue
light = trtl.Turtle()
light.speed("fastest")
light.screen.bgcolor("#05BFE8")

# Start of box
light.goto(-50,300)
def draw_sides():
#drew the outlines/edges of the traffic light
    light.forward(100)
    light.right(90)
    light.forward(305)
    light.right(90)
#Begin fill in object
light.begin_fill()
draw_sides()
draw_sides()
#end fill on object
light.end_fill()

#Made pole from the bottom of the light going to the ground
def draw_pole():
    light.goto(0,0)
    light.goto(0,0)
    light.forward(12.5)
    light.right(90)
    light.forward(300)
    light.right(90)
    light.forward(22)
    light.right(90)
    light.forward(300)
#filled in the light pole
light.begin_fill()
draw_pole()
light.end_fill()

#Made the grass
light.penup()
light.goto(-500, -400)
light.pensize(7)
light.color("green")
#Set the randomized blades of grass.

def draw_grass():
    length = random.randint(85, 140)

    light.setheading(90)
    light.pendown()
    light.forward(length)
    light.penup()
    light.right(180)
    light.forward(length)
    light.left(90)
    light.forward(10)
    light.left(90)
for blades in range(100):
    draw_grass()

#Made the red light for the traffic light
light.penup()
light.goto(40,250)
light.color("red")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

#Made the yellow light for the traffic light
light.penup()
light.goto(40,150)
light.color("yellow")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

#Made the green light for the traffic light
light.penup()
light.goto(40,50)
light.color("green")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

#Made the animation for the sun progressing across the sky like how it moves throughout the day
def draw_star(startx, starty):
    light.penup()
    light.goto(startx, starty)
    light.color("#FC9601")
    light.pendown()
    light.begin_fill()
    light.circle(40)
    light.end_fill()


# Determines how many times the sun moves across the sky
x = -600
y = 350
light.speed("normal")
for intervals in range(12):
    draw_star(x, y)
    for undo_number in range(4):
        light.undo()
    x += 100






wn = trtl.Screen()
wn.mainloop()