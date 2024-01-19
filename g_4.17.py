import turtle 

turtle.hideturtle()

for i in range(4):
    turtle.forward(100)
    turtle.left(180-45)
    turtle.forward((2*100**2)**0.5)
    turtle.left(-45)
    turtle.left(45)
    turtle.left(180-45)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)


