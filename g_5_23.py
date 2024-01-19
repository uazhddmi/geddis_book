import turtle as tr

def drawBase():
    tr.penup()
    tr.goto(-75,-150)
    tr.pendown()
    tr.circle(150)
    print(tr.pos())

def drawMidScection():
    tr.penup()
    tr.goto(-50, 50)
    tr.pendown()
    tr.circle(100)


def drawArms():
    pass

def drawHead():
    pass

def drawHat():
    pass

def main():
    tr.speed(4)
    tr.left(90)
    tr.forward(400)
    drawBase()
    drawMidScection()

if __name__ == '__main__':
    main()