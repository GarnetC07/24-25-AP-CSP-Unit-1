import turtle as trtl

painter = trtl.Turtle()

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
color = "gray"
# iterate
for floor in range(num_floors):
  # set placement and color of turtle
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
    if color =
  y = y + 5 # location of next floor









wn = trtl.Screen()
wn.mainloop()