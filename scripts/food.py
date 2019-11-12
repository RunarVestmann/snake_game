import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Food:
    def __init__(self, start_x=random.randint(0, SCREEN_WIDTH-1),\
                       start_y=random.randint(0, SCREEN_HEIGHT-1)):
        self.__x = start_x
        self.__y = start_y

    def get_position(self):
        '''Returns a tuple containing the x and y position of the food'''
        return self.__x, self.__y

    def respawn(self):
        '''Respawns the food at a random position'''
        self.__x = random.randint(0, SCREEN_WIDTH-1)
        self.__y = random.randint(0, SCREEN_HEIGHT-1)
