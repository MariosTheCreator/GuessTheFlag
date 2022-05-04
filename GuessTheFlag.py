import turtle
import time
import random

done = True

scr = turtle.Screen()
pen = turtle.Turtle()

scr.title('Flag Game')

print('Welcome to FLAG GAME')

coins = 50
help = 1

pen.speed(200)
pen.pensize(5)
pen.up()
pen.goto(-300, 50)

pen.pd()

pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(70)
pen.bk(70)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(70)

pen.up()
pen.fd(70)
pen.pd()

pen.rt(90)
pen.fd(200)
pen.lt(90)
pen.fd(90)

pen.up()
pen.fd(70)
pen.pd()

pen.lt(70)
pen.fd(200)
pen.rt(140)
pen.fd(200)
pen.bk(100)
pen.rt(110)
pen.fd(77)

pen.up()
pen.rt(180)
pen.fd(150)
pen.lt(90)
pen.fd(50)
pen.pd()

pen.rt(180)
pen.fd(150)
pen.lt(90)
pen.fd(100)
pen.lt(90)
pen.fd(50)
pen.lt(90)
pen.fd(40)

pen.up()
pen.fd(60)
pen.pd()

pen.rt(90)
pen.fd(140)
pen.rt(90)
pen.fd(90)

pen.up()
pen.goto(-300, -100)
pen.pd()

pen.rt(90)
pen.fd(150)
pen.lt(90)
pen.fd(100)
pen.lt(90)
pen.fd(50)
pen.lt(90)
pen.fd(40)

pen.up()
pen.fd(60)
pen.pd()

pen.rt(90)
pen.fd(140)
pen.rt(90)
pen.fd(90)

pen.up()
pen.goto(-150, -250)
pen.pd()

pen.lt(70)
pen.fd(200)
pen.rt(140)
pen.fd(200)
pen.bk(100)
pen.rt(110)
pen.fd(77)

pen.up()
pen.goto(20, -250)
pen.pd()

pen.rt(90)
pen.fd(200)
pen.rt(150)
pen.fd(120)
pen.lt(120)
pen.fd(120)
pen.rt(150)
pen.fd(200)

pen.up()
pen.goto(200, -250)
pen.pd()

pen.lt(90)
pen.fd(100)
pen.bk(100)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(100)
pen.bk(100)
pen.lt(90)
pen.fd(100)
pen.rt(90)
pen.fd(100)

while done == True:

    def france():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('blue')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def belgium():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.fillcolor('black')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(200)
        pen.fillcolor('yellow')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(200)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def japan():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.up()
        pen.goto(-100, 30)
        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.pencolor('red')
        pen.dot(150)
        pen.up()
        pen.goto(600, 500)


    def ireland():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('orange')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def romania():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('blue')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('yellow')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def italy():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def sweden():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.begin_fill()
        pen.fillcolor('blue')
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.fillcolor('yellow')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.rt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)

        pen.fillcolor('yellow')
        pen.pencolor('yellow')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(250)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def finland():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.begin_fill()
        pen.fillcolor('white')
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.fillcolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.rt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)

        pen.fillcolor('blue')
        pen.pencolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(250)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def england():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.begin_fill()
        pen.fillcolor('white')
        pen.pencolor('black')
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.fillcolor('red')
        pen.pencolor('white')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.rt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(200)
        pen.lt(90)

        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(250)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def iceland():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.begin_fill()
        pen.fillcolor('blue')
        pen.pencolor('black')
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.rt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)

        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(250)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def norway():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(200)
        pen.begin_fill()
        pen.fillcolor('red')
        pen.pencolor('black')
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.lt(90)
        pen.fd(100)
        pen.rt(90)
        pen.fillcolor('blue')
        pen.pencolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(350)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()

        pen.up()
        pen.rt(90)
        pen.fd(100)
        pen.lt(90)
        pen.fd(125)
        pen.lt(90)

        pen.fillcolor('blue')
        pen.pencolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(250)
            pen.lt(90)
            pen.fd(50)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def netherlands():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def monaco():
        pen.reset()
        pen.up()
        pen.goto(-150, -100)

        pen.speed(200)
        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()

        pen.lt(90)
        pen.fd(125)
        pen.rt(90)

        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def poland():
        pen.reset()
        pen.goto(-150, -100)

        pen.speed(200)
        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()

        pen.lt(90)
        pen.fd(125)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def germany():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('yellow')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('black')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def austria():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def estonia():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('blue')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def bulgaria():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('green')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def hungary():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('green')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def lithuania():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('green')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('yellow')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def mali():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('yellow')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def guinea():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('yellow')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def nigeria():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def ivory_coast():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('orange')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('white')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(100)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()


    def gabon():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('light blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('yellow')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def sierra_leone():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('light blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def yemen():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def luxembourg():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('light blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def russia():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def armenia():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.speed(100)
        pen.fillcolor('yellow')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('blue')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)

        pen.fillcolor('red')
        pen.begin_fill()
        for i in range(2):
            pen.fd(300)
            pen.lt(90)
            pen.fd(70)
            pen.lt(90)
        pen.up()
        pen.end_fill()

        pen.lt(90)
        pen.fd(70)
        pen.rt(90)


    def indonesia():
        pen.reset()
        pen.up()
        pen.goto(-150, -100)

        pen.speed(200)
        pen.fillcolor('white')
        pen.pencolor('black')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()

        pen.lt(90)
        pen.fd(125)
        pen.rt(90)

        pen.fillcolor('red')
        pen.pencolor('red')
        pen.pd()
        pen.begin_fill()
        for i in range(2):
            pen.fd(280)
            pen.lt(90)
            pen.fd(125)
            pen.lt(90)
        pen.end_fill()
        pen.up()


    def bangladesh():
        pen.reset()

        pen.up()
        pen.goto(-150, -100)

        pen.pd()
        pen.speed(100)
        pen.fillcolor('dark green')
        pen.begin_fill()
        for i in range(2):
            pen.fd(340)
            pen.lt(90)
            pen.fd(250)
            pen.lt(90)
        pen.pd()
        pen.end_fill()

        pen.up()
        pen.goto(-130, 30)
        pen.fd(100)
        pen.pd()
        pen.speed(100)
        pen.pencolor('red')
        pen.dot(150)
        pen.up()
        pen.goto(600, 500)


    b = True
    while b == True:
        points = 0
        lives = 3
        r = 0
        f = 0
        g = 0

        flags = [france, belgium, luxembourg, ireland, romania, italy, sweden, finland, england, iceland]
        flags2 = [norway, netherlands, monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania]
        flags3 = [france, belgium, japan, ireland, romania, italy, sweden, finland, england, iceland, norway,
                  netherlands,
                  monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania]
        flags4 = [mali, nigeria, guinea, ivory_coast, gabon, sierra_leone]
        flags5 = [yemen, japan, russia, armenia, indonesia, bangladesh]
        flags6 = [france, belgium, luxembourg, ireland, romania, italy, sweden, finland, england, iceland,
                  norway, netherlands, monaco, poland, germany, austria, estonia, bulgaria, hungary, lithuania,
                  mali, nigeria, guinea, ivory_coast, gabon, sierra_leone, yemen, japan, russia, armenia,
                  indonesia, bangladesh]

        goo = input("Choose a quiz, answer with 1, 2, 3, 4, 5, 6\nor type INFO for more information")
        print('You start with 3 lives, 0 points and', help, 'helps')

        if goo == '2':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 2')
            while lives > 0 and len(flags2) > 0:
                pen.reset()
                flag = random.choice(flags2)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags2.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags2.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == '1':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 1')
            while lives > 0 and len(flags) > 0:
                pen.reset()
                flag = random.choice(flags)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == '3':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 3')
            while lives > 0 and len(flags3) > 0:
                pen.reset()
                flag = random.choice(flags3)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags3.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags3.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == '4':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 4')
            while lives > 0 and len(flags4) > 0:
                pen.reset()
                flag = random.choice(flags4)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags4.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags4.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == '5':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 5')
            while lives > 0 and len(flags5) > 0:
                pen.reset()
                flag = random.choice(flags5)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags5.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags5.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == '6':
            pen.up()
            pen.reset()
            pen.pensize(5)
            pen.goto(100, 0)
            pen.pd()

            pen.speed(200)
            pen.bk(100)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)
            pen.bk(100)
            pen.rt(90)
            pen.fd(100)
            pen.lt(90)
            pen.fd(100)

            print('3')
            time.sleep(1)
            pen.reset()
            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(100, 0)
            pen.pd()

            pen.lt(180)
            pen.fd(180)
            pen.rt(135)
            pen.fd(230)
            pen.lt(45)
            pen.fd(60)
            pen.lt(90)
            pen.fd(160)
            pen.lt(90)
            pen.fd(60)
            print('2')

            time.sleep(1)
            pen.reset()

            pen.speed(200)
            pen.pensize(5)
            pen.up()
            pen.goto(0, 0)
            pen.pd()

            pen.lt(90)
            pen.fd(200)
            pen.lt(135)
            pen.fd(90)

            print('1')
            time.sleep(1)
            print('GO')
            startTime = time.time()
            print('Points:', points)
            print('Lives:', lives)
            print('Helps:', help)
            print('Coins:', coins)
            print('You chose Quiz 6')
            help += 2
            while lives > 0 and len(flags6) > 0:
                pen.reset()
                flag = random.choice(flags6)
                flag()
                answer = input("Answer the question")

                if answer == flag.__name__:
                    points += 1
                    coins += 10
                    flags6.remove(flag)
                    r += 1
                    print('Correct')
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
                elif answer == 'help':
                    if help >= 1:
                        points += 1
                        coins += 10
                        flags6.remove(flag)
                        r += 1
                        help -= 1
                        print('Correct')
                        print('Points:', points)
                        print('Lives:', lives)
                        print('Helps:', help)
                        print('Coins:', coins)
                    else:
                        print('You have run out of helps')
                else:
                    print('Try again')
                    if points > 0:
                        points -= 1
                    else:
                        points = 0
                    lives -= 1
                    if coins >= 20:
                        coins -= 5
                    else:
                        coins = 20
                    f += 1
                    print('Points:', points)
                    print('Lives:', lives)
                    print('Helps:', help)
                    print('Coins:', coins)
        elif goo == 'INFO':
            print(
                'Both Quiz 1 and Quiz 2 have 10 european countries,\nQuiz 2 is a bit harder than Quiz 1.\nQuiz 3 has '
                '20 '
                'countries\nQuiz 4 has 6 African countries\nQuiz 5 has 6 Asian countries\nQuiz 6 has 32 countries('
                'LEVEL IMPOSSIBLE')
        else:
            print('Something is wrong')
        endtime = time.time()
        if lives == 0:
            print('Correct:', r, " False:", f, 'Time:', round(endtime - startTime, 2))
        elif r>g:
            print('It is time for your prize')
            l=True
            while l == True:
                asko = input('Choose 1, 2 or 3\n1.Earn 1 Help\n2.Earn 50 coins\n3.Earn 1 life ')
                if asko == '1':
                    help+=1
                    print('You earned your prize')
                    l = False
                elif asko == '2':
                    coins+=50
                    print('You earned your prize')
                    l = False
                elif asko=='3':
                    lives+=1
                    print('You earned your prize')
                    l=False
                else:
                    print('Something went wrong')
        a = True
        while a == True:
            go = input("Do you want to try again,\nanswer with YES or NO\nor with BUY to open store")
            if go == 'NO':
                q = True
                while q == True:
                    ask = input('Did you enjoy that QUIZ GAME?\nAnswer with YES or NO')
                    if ask == 'YES':
                        print('Thanks for your review')
                        quit()
                    elif ask == 'NO':
                        print('I do not care')
                        quit()
                    else:
                        print('Something went wrong')
            elif go == 'YES':
                print('Lets go')
                a = False
            elif go == 'BUY':
                d = True
                pen.reset()
                pen.speed(200)
                pen.pensize(5)

                pen.up()
                pen.goto(-350, 0)
                pen.pd()

                pen.fd(100)
                pen.lt(90)
                pen.fd(80)
                pen.lt(90)
                pen.fd(100)
                pen.rt(90)
                pen.fd(80)
                pen.rt(90)
                pen.fd(100)

                pen.up()
                pen.fd(40)
                pen.pd()

                pen.fd(100)
                pen.bk(50)
                pen.rt(90)
                pen.fd(160)

                pen.lt(90)
                pen.up()
                pen.fd(90)
                pen.pd()

                for i in range(2):
                    pen.fd(100)
                    pen.lt(90)
                    pen.fd(160)
                    pen.lt(90)

                pen.up()
                pen.fd(140)
                pen.pd()

                pen.lt(90)
                pen.fd(160)
                for i in range(3):
                    pen.rt(90)
                    pen.fd(80)
                pen.lt(135)
                pen.fd(100)

                pen.up()
                pen.lt(45)
                pen.fd(40)
                pen.pd()

                pen.fd(100)
                pen.bk(100)
                pen.lt(90)
                pen.fd(75)
                pen.rt(90)
                pen.fd(100)
                pen.bk(100)
                pen.lt(90)
                pen.fd(75)
                pen.rt(90)
                pen.fd(100)

                while d == True:
                    print('COIN STORE\n1 HELP = 50 COINS\n2 HELPS = 100 COINS\n4 HELPS = 150 COINS\n5 HELPS = 200 '
                          'COINS\nCOINS:', coins, '\nHelps:', help, '\nanswer with 1, 2, 4, 5 or EXIT')
                    buy = input()
                    if buy == '1':
                        if coins >= 50:
                            coins -= 50
                            help += 1
                            print('Coins:', coins)
                            print('Helps:', help)
                            print('You successfully purchased pack 1')
                        else:
                            print('You do not have enough coins')
                    elif buy == '2':
                        if coins >= 100:
                            coins -= 100
                            help += 2
                            print('Coins:', coins)
                            print('Helps:', help)
                            print('You successfully purchased pack 2')
                        else:
                            print('You do not have enough coins')
                    elif buy == '4':
                        if coins >= 150:
                            coins -= 150
                            help += 4
                            print('Coins:', coins)
                            print('Helps:', help)
                            print('You successfully purchased pack 3')
                        else:
                            print('You do not have enough coins')
                    elif buy == '5':
                        if coins >= 200:
                            coins -= 200
                            help += 5
                            print('Coins:', coins)
                            print('Helps:', help)
                            print('You successfully purchased pack 4')
                        else:
                            print('You do not have enough coins')
                    elif buy == 'EXIT':
                        print('You are leaving store in..')
                        print('3')
                        time.sleep(1)
                        print('2')
                        time.sleep(1)
                        print('1')
                        time.sleep(1)
                        d = False
                        pen.reset()
                    else:
                        print('Something is wrong')
            else:
                print('Something is wrong')

turtle.done()
