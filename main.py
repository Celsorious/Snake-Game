import time 
from turtle import Screen
import snake
from food import Food
from scoreboard import Scoreboard


# CONFIGURACIÓN SNAKE #
snake_0 = snake.Snake() 


# CONFIGURACIÓN SCREEN #
screen = Screen()
screen.setup(height = 600, width = 600)
screen.bgcolor("black") # BACKGROUND COLOR
screen.title("Snake game")
screen.tracer(0) # APAGADO
screen.listen()
screen.onkey(snake_0.up, "Up")
screen.onkey(snake_0.down, "Down")
screen.onkey(snake_0.left, "Left")
screen.onkey(snake_0.right, "Right")

# CONFIGURACIÓN COMIDA #
food = Food()

# CONFIGURACIÓN CONTADOR #
scoreboard = Scoreboard()

game_on = True
score = 0

while game_on:
    screen.update()
    time.sleep(0.1) # DELAY REFRESH SCREEN

    snake_0.move()

    # DETECT COLLISION WITH FOOD #
    if snake_0.head.distance(food.position()) < 15: # Distancia de la snake con respecto a la comida
       food.refresh()
       scoreboard.refresh_score()
       snake_0.extend()

    # DETECT COLLISION WITH WALL #
    if snake_0.head.xcor() > 290 or snake_0.head.xcor() < -290 or snake_0.head.ycor() > 290 or snake_0.head.ycor() < -290:
        game_on = False
        scoreboard.game_over()
    
    # DETECT COLLISION WITH TAIL #
    for segment in snake_0.segments[1:]:
        if snake_0.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


        



screen.exitonclick()