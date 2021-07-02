from turtle import Turtle
# from turtle import Screen
import time


class Plane(Turtle):
    def __init__(self):
        super().__init__()
        # wn = Screen()
        # wn.addshape('plane.gif')
        self.shape("square")
        self.shapesize(1,3)
        self.color("blue")
        self.penup()
        self.goto(0,-260)
        self.bullets = []


    def move_left(self):
        if self.xcor() > -260:
            self.setx(self.xcor()-20)

    def move_right(self):
        if self.xcor() < 260:
            self.setx(self.xcor()+20)

    def shoot(self):
        bullet = Turtle("square")
        bullet.shapesize(0.25,0.25)
        bullet.penup()
        bullet.setpos(self.xcor(),self.ycor())
        bullet.speed("slowest")
        bullet.color("blue")
        self.bullets.append(bullet)

    def bullet_fly(self):
        if self.bullets !=[]:
            for bullet in self.bullets:
                if bullet.ycor() < 300:
                    bullet.sety(bullet.ycor()+ 60)
                else:
                    bullet.color("black")