import turtle as trtl
import random

# named turtle light
light = trtl.Turtle()
light.speed("fastest")
light.screen.bgcolor("lightblue")
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


light.penup()
light.goto(-500, -400)
light.pensize(7)
light.color("green")
#Drawing the randomized blades of grass.

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

#Made the yellow light for the traffic light
light.penup()
light.goto(40,250)
light.color("red")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

light.penup()
light.goto(40,150)
light.color("yellow")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

light.penup()
light.goto(40,50)
light.color("green")
light.pendown()
light.begin_fill()
light.circle(40)
light.end_fill()

wn = trtl.Screen()
wn.mainloop()