from turtle import Turtle
import random

ROW = 3

class Blocks:
    def __init__(self):
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        init_y = 60
        x_list = list(range(-280,280,20))
        for y in range(ROW):
            for x in range(5):
                block = Turtle("square")
                block.color("white")
                block.shapesize(0.5,0.5)
                block.penup()
                block.setpos(random.choice(x_list), init_y-20*y)
                self.blocks.append(block)
