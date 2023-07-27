import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')

fred = turtle.Turtle()
fred.speed(2)

wn.reset()
turtle.setworldcoordinates(-1,-1.25,360,1.25)

for angle in range(0,361):
    seno = math.sin(math.radians(angle))
    fred.goto(angle,seno)

wn.exitonclick()