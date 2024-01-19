import turtle
turtle.speed(0)
dist = 5
turtle.right(180)
for i in range(100):
    for j in range(4):
        turtle.forward(dist)
        turtle.right(90)
    dist += 5
