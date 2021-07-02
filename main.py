from turtle import Screen
from plane import Plane
from aliens import Aliens
from blocks import Blocks
from scoreboard import ScoreBoard
import time



screen = Screen()
screen.title("Space Invaders")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

plane = Plane()
aliens = Aliens()
blocks = Blocks()

scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(plane.move_left, "Left")
screen.onkeypress(plane.move_right, "Right")
screen.onkeypress(plane.shoot, "space")

GameOver = False
TouchWall = False




while not GameOver:
    screen.update()
    time.sleep(0.1)
    aliens.aliens_move()
    aliens.bullet_fly()
    plane.bullet_fly()

    if aliens.aliens !=[]:
        for alien in aliens.aliens:
            if alien.xcor() > 250 or alien.xcor() < -250:
                TouchWall = True

            if alien.distance(plane) <= 20:
                scoreboard.life -= 1
                scoreboard.change_score_life()
                plane.setpos(0,-260)
                time.sleep(0.5)
        for bullet in aliens.bulletss:
            if bullet.distance(plane) <= 20:
                scoreboard.life -= 1
                scoreboard.change_score_life()
                plane.setpos(0, -260)
                time.sleep(0.5)

        if TouchWall:
            aliens.touch_wall()
            TouchWall = False

        #plane bullets
        for bullet in plane.bullets:
            for block in blocks.blocks:
                if bullet.distance(block) <= 20:
                    bullet.setpos(400,400)
                    plane.bullets.remove(bullet)
                    blocks.blocks.remove(block)
                    block.hideturtle()
                    bullet.hideturtle()
        for bullet in plane.bullets:
            for alien in aliens.aliens:
                if bullet.distance(alien) <= 20:
                    bullet.setpos(400,400)
                    plane.bullets.remove(bullet)
                    aliens.aliens.remove(alien)
                    alien.hideturtle()
                    bullet.hideturtle()
                    scoreboard.score += 100
                    scoreboard.change_score_life()

        #aliens bullets
        for bullet in aliens.bulletss:
            for block in blocks.blocks:
                if bullet.distance(block) <= 20:
                    bullet.setpos(400,400)
                    aliens.bulletss.remove(bullet)
                    blocks.blocks.remove(block)
                    block.hideturtle()
                    bullet.hideturtle()


    else:
        scoreboard.game_win()
        GameOver = True

    if scoreboard.life <= 0:
        scoreboard.game_over()
        GameOver = True











screen.exitonclick()