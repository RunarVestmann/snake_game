import pygame
from food import Food
from snake import Snake
from settings import *

#Initialize the screen
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Initialize font library
pygame.font.init()
FONT_DATA = pygame.font.SysFont(FONT, FONT_SIZE)

#Set the title and the icon
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("../images/SnakeIcon.png"))

#Global variables for resetting the game
GAME_OVER = False
FOOD = Food()
SNAKE = Snake(160, 160)

def handle_user_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                SNAKE.update_velocity(-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT:
                SNAKE.update_velocity(CELL_SIZE, 0)
            if event.key == pygame.K_DOWN:
                SNAKE.update_velocity(0, CELL_SIZE)
            if event.key == pygame.K_UP:
                SNAKE.update_velocity(0, -CELL_SIZE)

            if event.key == pygame.K_ESCAPE:
                quit_game()

            if event.key == pygame.K_SPACE:
                reset_game()

        if event.type == pygame.QUIT:
            quit_game()

def quit_game():
    pygame.quit()
    quit()

def reset_game():
    '''Resets the game by setting the snake's length to 1 and respawning the food'''

    #Using the global keyword instead of recursively calling the game_loop
    #function, so the game won't crash due to too many stack frames
    global GAME_OVER
    GAME_OVER = False
    FOOD.respawn()
    global SNAKE
    SNAKE = Snake(160, 160)

def draw_objects():
    SCREEN.fill(BACKGROUND_COLOR)

    #Draw the FOOD
    pygame.draw.rect(SCREEN, FOOD_COLOR, pygame.Rect(FOOD.get_position(), CELL_DIMENSIONS))

    #Draw the SNAKE
    for segment in SNAKE.get_segments():
        pygame.draw.rect(SCREEN, SNAKE_COLOR, pygame.Rect(segment, CELL_DIMENSIONS), 1)

def game_loop():
    global GAME_OVER
    final_score = None

    while True:
        handle_user_input()

        if not GAME_OVER:
            SNAKE.update_position()
            draw_objects()
        else:
            SCREEN.blit(final_score, END_GAME_TEXT_POSITION)

        pygame.display.update()

        pygame.time.wait(TIME_BETWEEN_FRAMES)

        if SNAKE.crashed_into_self() or SNAKE.crashed_into_wall():
            GAME_OVER = True
            final_score = FONT_DATA.render(END_GAME_TEXT + str(len(SNAKE)), False, END_GAME_TEXT_COLOR)

        elif SNAKE.found_food(FOOD.get_position()):
            FOOD.respawn(SNAKE.get_segments())

game_loop()
