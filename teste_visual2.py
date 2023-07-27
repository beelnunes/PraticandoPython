import turtle
wn = turtle.Screen()

tess = turtle.Turtle()
tess.speed(1)

turtle.shape("square")
turtle.shapetransform(4, -1, 0, 2)
turtle.get_shapepoly()
((50, -20), (30, 20), (-50, 20), (-30, -20))

tess.forward(100)