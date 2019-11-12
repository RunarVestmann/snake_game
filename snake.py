from settings import *

class Snake:
    def __init__(self, start_x, start_y, x_dir=0, y_dir=0):
        self.__x = start_x
        self.__y = start_y
        self.__x_dir = x_dir
        self.__y_dir = y_dir

    def crashed_into_self(self):
        '''Returns True if the snake has crashed into itself'''
        return False

    def crashed_into_wall(self):
        '''Returns True if the snake has crashed into a wall'''
        return self.__x < 0 or self.__x >= SCREEN_WIDTH or self.__y < 0 or self.__y >= SCREEN_HEIGHT

    def get_position(self):
        '''Returns a tuple containing the snake's x and y position'''
        return self.__x, self.__y

    def update_direction(self, x_dir, y_dir):
        '''Updates  which direction the snake is facing'''
        if x_dir == self.__x_dir and y_dir == self.__y_dir:
            return
        self.__x_dir = x_dir
        self.__y_dir = y_dir

    def update_position(self):
        '''Moves the snake in the direction it is facing'''
        self.__x += self.__x_dir
        self.__y += self.__y_dir
    