import turtle as tr


def triangle(p1, p2, c='yellow'):
    tr.Turtle.fillcolor(c)
    tr.begin_fill()
    tr.goto(p1)
    tr.goto(p2)
    tr.goto(0,0)
    tr.end_fill()

def main():
    p1 = input('Enter 1st coordiante (x, y)').strip().split(',')
    p2 = input('Enter 2nd coordiante (x, y)').strip().split(',')
    color = '"'+ input('Enter fill color: ').strip() + '"'
    print(color, type(color))

    triangle(p1, p2, color)

if __name__ == '__main__':
    main()