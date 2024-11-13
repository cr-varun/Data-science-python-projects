from turtle import Turtle,Screen



GAME_ON=True
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")


    def Gameon(self):
        self.setheading(30)
        self.penup()
        self.speed(1)

        for _ in range(50):
            self.forward(5)

    def stop(self):
        GAME_ON=False

