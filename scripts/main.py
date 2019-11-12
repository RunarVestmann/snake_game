import pygame
from food import Food
from snake import Snake
from settings import *

#Initialize the screen
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set the title and the icon
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("../images/SnakeIcon.png"))

def handle_user_input(snake):
    '''Handles each input from the user'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.update_velocity(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.update_velocity(1, 0)
            if event.key == pygame.K_DOWN:
                snake.update_velocity(0, 1)
            if event.key == pygame.K_UP:
                snake.update_velocity(0, -1)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def game_loop():

    food = Food()
    snake = Snake(200, 200)

    while True:
        SCREEN.fill(BACKGROUND_COLOR)

        handle_user_input(snake)

        snake.update_position()

        #Draw the food
        pygame.draw.rect(SCREEN, FOOD_COLOR, pygame.Rect(food.get_position(), CELL_SIZE))

        #Draw the snake
        for segment in snake.get_segments():
            pygame.draw.rect(SCREEN, SNAKE_COLOR, pygame.Rect(segment, CELL_SIZE))

        pygame.display.update()

        if snake.found_food(food.get_position()):
            food.respawn()

        elif snake.crashed_into_self() or snake.crashed_into_wall():
            print("Game Over")

        pygame.time.wait(1000)

game_loop()
