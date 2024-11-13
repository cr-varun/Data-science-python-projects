from turtle import Turtle, Screen



STARTING_POSITIONS_Right = [(380, 20), (380, 0), (380, -20)]
STARTING_POSITIONS_Left = [(-380, 20), (-380, 0), (-380, -20)]
screenprob=Screen()
screenprob.tracer(0)
class Pong:

    def __init__(self):
        self.pongRight = []
        self.pongLeft = []
        self.createPond()
    def createPond(self):
        for pos in STARTING_POSITIONS_Right:
            self.pong=Turtle("square")
            self.pong.color("white")
            self.pong.penup()
            self.pong.goto(pos)
            self.pong.setheading(90)
            self.pongRight.append(self.pong)
        self.PongRightHead = self.pongRight[0]
        for pos in STARTING_POSITIONS_Left:
            self.pong=Turtle("square")
            self.pong.color("white")
            self.pong.penup()
            self.pong.goto(pos)
            self.pong.setheading(90)
            self.pongLeft.append(self.pong)
        self.PongleftHead=self.pongLeft[0]
        screenprob.update()
    def left_up(self):
        if(self.PongleftHead.pos()<(-380, 320)):
            for i in self.pongLeft:
                i.forward(10)
            screenprob.update()
            print("forward")
    def left_down(self):
        if(self.PongleftHead.pos()>(-380, -270)):
            for i in self.pongLeft:
                i.backward(10)
            screenprob.update()
    def right_up(self):
        if(self.PongRightHead.pos()<(380, 320)):
            for i in self.pongRight:
                i.forward(10)
            screenprob.update()
            print("forward")
    def right_down(self):
        if(self.PongRightHead.pos()>(380, -270)):
            for i in self.pongRight:
                i.backward(10)
            screenprob.update()