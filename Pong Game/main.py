import turtle
from pongClass import Pong
from ball import Ball
newt = turtle.Turtle()
screenprob = turtle.Screen()
screenprob.listen()
def screenSetup():

    screenprob.setup(800,600)
    screenprob.bgcolor("black")
    screenprob.title("Pong game")
    newt.color("white")
    newt.pensize(3)
    newt.penup()
    x=newt.pos()
    newt.goto(0,300)
    newt.setheading(270)
    return x

x=screenSetup()
while newt.distance(x)<330:
    newt.pendown()
    newt.forward(10)
    newt.penup()
    newt.forward(10)
pong = Pong()
ball = Ball()
ball.Gameon()
screenprob.onkeypress(key="w", fun=pong.left_up)
screenprob.onkeypress(key="s", fun=pong.left_down)
screenprob.onkeypress(key="Up", fun=pong.right_up)
screenprob.onkeypress(key="Down", fun=pong.right_down)
screenprob.onkeypress(key="f", fun=ball.stop)

screenprob.exitonclick()