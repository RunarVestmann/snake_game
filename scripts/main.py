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

def handle_user_input(snake, game_states_dict):
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
                game_states_dict["Reset"] = True

        if event.type == pygame.QUIT:
            quit_game()

def quit_game():
    pygame.quit()
    quit()

def draw_objects(food, snake):
    SCREEN.fill(BACKGROUND_COLOR)

    #Draw the FOOD
    pygame.draw.rect(SCREEN, FOOD_COLOR, pygame.Rect(food.get_position(), CELL_DIMENSIONS))

    #Draw the SNAKE
    for segment in snake.get_segments():
        pygame.draw.rect(SCREEN, SNAKE_COLOR, pygame.Rect(segment, CELL_DIMENSIONS), 1)

def game_loop():

    food = Food()
    snake = Snake(160, 160)

    game_states_dict = {"Game_Over":False, "Reset":False}
    final_score = None

    while True:

        handle_user_input(snake, game_states_dict)

        #If the user pressed spacebar we reset the game
        if game_states_dict["Reset"]:
            snake = Snake(160, 160)
            food.respawn(snake.get_segments())
            game_states_dict["Game_Over"] = False
            game_states_dict["Reset"] = False

        if not game_states_dict["Game_Over"]:
            snake.update_position()
            draw_objects(food, snake)
        else:
            SCREEN.blit(final_score, END_GAME_TEXT_POSITION)

        pygame.display.update()

        pygame.time.wait(TIME_BETWEEN_FRAMES)

        if snake.crashed_into_self() or snake.crashed_into_wall():
            game_states_dict["Game_Over"] = True
            final_score = FONT_DATA.render(END_GAME_TEXT + str(len(snake)), False, END_GAME_TEXT_COLOR)

        elif snake.found_food(food.get_position()):
            food.respawn(snake.get_segments())

game_loop()
