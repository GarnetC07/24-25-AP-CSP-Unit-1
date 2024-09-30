#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
turt = trtl.Turtle()
turt.pensize(40)
turt.circle(20)
# creates the circle of the body for the spider changing size of circle and how thick it is
lines = 8
length = 70
#number of legs and the length of them
angle = 360 / lines
#take number of legs and divides by 380
turt.pensize(5)
n = 0
while (n < lines):
  turt.goto(0,20)
  turt.setheading(angle*n)
  turt.forward(length)
  n = n + 1
turt.hideturtle()
wn = trtl.Screen()
wn.mainloop()
