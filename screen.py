from snake import Snake
from turtle import Screen
import time

class Screen_game:
    def __init__(self):
        self.configure()
    
    def configure(self):
        screen = Screen()
        screen.setup(height = 600, width = 600)
        screen.bgcolor("black") # BACKGROUND COLOR
        screen.title("Snake game")
        screen.tracer(0) # APAGADO
        screen.listen()

        snake_0 = Snake()

        screen.onkey(snake_0.up, "Up")
        screen.onkey(snake_0.down, "Down")
        screen.onkey(snake_0.left, "Left")
        screen.onkey(snake_0.right, "Right")


        game_on = True

        while game_on:
            screen.update()
            time.sleep(0.2)

            snake_0.move()



                



        screen.exitonclick()
