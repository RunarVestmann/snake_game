import pygame
from food import Food
from snake import Snake
from settings import *

#Initialize the screen
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Set the title and the icon
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("images/SnakeIcon.png"))

def handle_user_input(snake):
    '''Handles each input from the user'''
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.update_direction(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.update_direction(1, 0)
            if event.key == pygame.K_DOWN:
                snake.update_direction(0, 1)
            if event.key == pygame.K_UP:
                snake.update_direction(0, -1)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

def snake_crashed_into_wall(snake_position):
    snake_x, snake_y = snake_position
    return snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT

def game_loop():

    food = Food()
    snake = Snake(200, 200)

    while True:
        SCREEN.fill(BACKGROUND_COLOR)

        handle_user_input(snake)

        snake.update_position()

        pygame.display.update()

        if snake.crashed_into_wall() or snake.crashed_into_self():
            print("Game Over")

        pygame.time.wait(1000)

game_loop()
