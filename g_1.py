if x > 100:
    y = 20
    z= 40

if a < 10:
    b = 0 
    c = 1

#3
if a < 10:
    b = 0
else:
    b = 99

#4
if score >= A_score:
    print("you level A")
    if score >= B_score:
        print("your level B")
        if score >= C_score:
            print('your level C')
            if score >= D_score:
                print('your score D')
            else:
                print('Your level F')


#5
if amount1 > 10 and amount2 <100:
    if amount1 > amount2:
        print(amount1)
    elif amount1 == amount2:
        print('they are equal')
    else:
        print(amount2)

#6
if speed > = 24 and speed <= 56:
    print('speed is normal')
else:
    print('speed is dangerous')

#7
if points < 9 or points > 51:
    print('out of limits')
else:
    print('points are in the range')


#8
import turtle
if turtle.angle() >= 0 and turtle.heading() <= 45:
    turtle.up()

#9
if turtle.pencolor() == 'red' or turtle.pencolor() == 'blue':
    turtle.pensize(5)

#10
if 100 <= turtle.xcor() <= 200 and 100 <= turtle.ycor() <= 200:
    turtle.hideturtle()
