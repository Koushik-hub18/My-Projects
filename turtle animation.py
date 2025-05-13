from turtle import *
from random import randint
import turtle

speed(10)
penup()
goto(-140,140)

for step in range(15):
    write(step,align='center')
    right(90)

    for num in range(8):
        penup()
        forward(10)
        penup()
        forward(10)

    penup()
    backward(160)
    left(90)
    forward(20)

#creating first turtle 
p1=Turtle()
p1.color('red')
p1.shape('turtle')

#setting the first turtle position
p1.penup()
p1.goto(-160,100)
p1.pendown()

#360 turn
for i in range(10):
    p1.right(36)

#creating second turtle
p2=Turtle()
p2.color("green")
p2.shape('turtle')

#setting the second turtle position 
p2.penup()
p2.goto(-160,70)
p2.pendown()

#360 turn
for turn in range(10):
    p2.right(36)

#creating third turtle
p3=Turtle()
p3.color=("yellow")
p3.shape('turtle')

#setting the third turtle position 
p3.penup()
p3.goto(-160,40)
p3.pendown()

#360 turn
for i in range(10):
    p3.right(36)
 
#creating forth turtle
p4=Turtle()
p4.color("blue")
p4.shape('turtle')

#setting the forth turtle position 
p4.penup()
p4.goto(-160,10)
p4.pendown()

#360 turn
for i in range(10):
    p4.right(36)

penup()
for turn in range(100):
    p1.forward(randint(1,5))
    p2.forward(randint(1,5))
    p3.forward(randint(1,5))
    p4.forward(randint(1,5))

done()