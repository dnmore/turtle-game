from turtle import Turtle
import random

STARTING_PACE = 5
SPEED_INCREASE = 10


class BombManager():
    def __init__(self):
        self.all_bombs = []
        self.bomb_speed = STARTING_PACE

    def create_bombs(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_bomb = Turtle('circle')
            new_bomb.color('red')
            new_bomb.penup()
            new_bomb.setheading(270)
            random_x = random.randint(-250, 250)
            new_bomb.goto(random_x, 300)
            self.all_bombs.append(new_bomb)

    def move_bombs(self):
        for bomb in self.all_bombs:
            bomb.forward(self.bomb_speed)

    def level_up(self):
        self.bomb_speed += SPEED_INCREASE
