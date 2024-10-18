import turtle as trtl
import random

# named turtle light
light = trtl.Turtle()
light.speed("fastest")
light.screen.bgcolor("lightblue")
# Start of box
light.goto(-50, 350)
def draw_sides():
#drew the outlines/edges of the traffic light
    light.forward(100)
    light.right(90)
    light.forward(300)
    light.right(90)
#Begin fill in object
light.begin_fill()
draw_sides()
draw_sides()
#end fill on object
light.end_fill()

#Made the red light for the traffic light
light.goto(3,300)
light.shape("circle")
light.color("red")

light.penup()
light.goto(-500, -400)
light.pensize(5)
light.color("Green")

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
    light.forward(20)
    light.left(90)
for blades in range(100):
    draw_grass()

wn = trtl.Screen()
wn.mainloop()