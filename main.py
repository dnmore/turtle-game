from turtle import Screen
from player import Player
from bomb_manager import BombManager
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
bomb_manager = BombManager()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
screen.onkey(player.move, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    bomb_manager.create_bombs()
    bomb_manager.move_bombs()
    for bomb in bomb_manager.all_bombs:
        if bomb.distance(player) < 10:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        bomb_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
