from turtle import Turtle
import random

ROW = 3

class Aliens:
    def __init__(self):
        self.aliens = []
        self.bulletss = []
        self.create_aliens()
        self.movex = 20
        self.movey = 0

    def create_aliens(self):
        ini_x = -240
        ini_y = 260
        for y in range(ROW):
            for x in range(5):
                alien = Turtle("triangle")
                alien.left(90)
                alien.color("red")
                alien.penup()
                alien.setpos(ini_x+35*x, ini_y-35*y)
                self.aliens.append(alien)

    def aliens_move(self):
        for alien in self.aliens:
            alien.goto(alien.xcor()+self.movex, alien.ycor()+self.movey)
            shoot_or_not = random.randint(0,20)
            if shoot_or_not == 1:
                self.shoot((alien.xcor(),alien.ycor()))

        self.movey = 0


    def touch_wall(self):
        self.movex *= -1
        self.movey = -20

    def shoot(self, position):
        bullet = Turtle("square")
        bullet.shapesize(0.25,0.25)
        bullet.penup()
        bullet.setpos(position)
        bullet.speed("slowest")
        bullet.color("red")
        self.bulletss.append(bullet)

    def bullet_fly(self):
        if self.bulletss !=[]:
            for bullet in self.bulletss:
                if bullet.ycor() > -300:
                    bullet.sety(bullet.ycor()- 20)
                else:
                    bullet.color("black")