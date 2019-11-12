import random
from settings import *

class Food:
    def __init__(self, start_x=random.randint(0, SCREEN_WIDTH-1),\
                       start_y=random.randint(0, SCREEN_HEIGHT-1)):
        self.__x = start_x
        self.__y = start_y

    def respawn(self):
        '''Respawns the food at a random position'''
        self.__x = random.randint(0, SCREEN_WIDTH-1)
        self.__y = random.randint(0, SCREEN_HEIGHT-1)

