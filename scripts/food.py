import random
from settings import CELL_SIZE, GRID_WIDTH, GRID_HEIGHT

class Food:
    def __init__(self):
        self.__x, self.__y = self.__calculate_random_position()
        self.__grid_x = 0
        self.__grid_y = 0

    def get_position(self):
        '''Returns a tuple containing the x and y position of the food'''
        return self.__x, self.__y

    def __calculate_random_position(self):
        '''Returns a tuple containing a new random x and y position'''
        return random.randint(0, GRID_WIDTH-1) * CELL_SIZE, random.randint(0, GRID_HEIGHT-1) * CELL_SIZE

    def respawn(self, snake_segments):
        '''Respawns the food at a random position that's not on top of the snake'''
        random_position = self.__calculate_random_position()
        while random_position in snake_segments:
            random_position = self.__calculate_random_position()
        self.__x, self.__y = random_position
