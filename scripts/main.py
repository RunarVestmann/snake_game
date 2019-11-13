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

# #Set the title and the icon
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("../images/SnakeIcon.png"))

def handle_user_input(constant_objects_dict):
    snake = constant_objects_dict["Snake"]
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake.update_velocity(-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake.update_velocity(CELL_SIZE, 0)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake.update_velocity(0, CELL_SIZE)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                snake.update_velocity(0, -CELL_SIZE)

            if event.key == pygame.K_ESCAPE:
                quit_game()

            if event.key == pygame.K_SPACE:
                reset_game(constant_objects_dict)

        if event.type == pygame.QUIT:
            quit_game()

def quit_game():
    pygame.quit()
    quit()

def reset_game(constant_objects_dict):
    constant_objects_dict["GAME_OVER"] = False
    constant_objects_dict["Food"] = Food()
    constant_objects_dict["Snake"] = Snake(160, 160)

def draw_objects(food, snake):
    SCREEN.fill(BACKGROUND_COLOR)

    #Draw the FOOD
    pygame.draw.rect(SCREEN, FOOD_COLOR, pygame.Rect(food.get_position(), CELL_DIMENSIONS))

    #Draw the SNAKE
    for segment in snake.get_segments():
        pygame.draw.rect(SCREEN, SNAKE_COLOR, pygame.Rect(segment, CELL_DIMENSIONS), 1)

def game_loop():

    #Dictionary with values containing the food, snake and whether the game is over or not
    constant_objects_dict = dict()
    reset_game(constant_objects_dict)
    final_score = None

    while True:

        #Fetch from the dictionary all the objects we need
        game_over = constant_objects_dict["GAME_OVER"]
        food = constant_objects_dict["Food"]
        snake = constant_objects_dict["Snake"]

        handle_user_input(constant_objects_dict)

        if not game_over:
            snake.update_position()
            draw_objects(food, snake)
        else:
            SCREEN.blit(final_score, END_GAME_TEXT_POSITION)

        pygame.display.update()

        pygame.time.wait(TIME_BETWEEN_FRAMES)

        if snake.crashed_into_self() or snake.crashed_into_wall():
            constant_objects_dict["GAME_OVER"] = True
            final_score = FONT_DATA.render(END_GAME_TEXT + str(len(snake)), False, END_GAME_TEXT_COLOR)

        elif snake.found_food(food.get_position()):
            food.respawn(snake.get_segments())

game_loop()
