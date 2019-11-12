from settings import CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Snake:

    def __init__(self, start_x, start_y, x_velocity=CELL_SIZE, y_velocity=0):

        #The body parts of the snake, index 0 is the head
        self.__segments = [(start_x, start_y)]

        self.__x_velocity = x_velocity
        self.__y_velocity = y_velocity

    def crashed_into_self(self):
        '''Returns True if the snake has crashed into itself, returns False otherwise'''
        return self.__segments[0] in self.__segments[1:]

    def crashed_into_wall(self):
        '''Returns True if the snake has crashed into a wall, returns False otherwise'''
        head_x, head_y = self.__segments[0]
        return head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT

    def get_segments(self):
        '''Returns a list of tuples containing the x and y position of each snake segment'''
        return self.__segments

    def found_food(self, food_position):
        '''Returns True if the snake has found food, returns False otherwise'''
        found_food = food_position == self.__segments[0]
        if found_food:
            self.__segments.append((0, 0))

        return found_food

    def update_velocity(self, x_velocity, y_velocity):
        '''Updates which direction the snake is moving'''

        #Only change direction if not going in the opposite direction
        if not (x_velocity == -self.__x_velocity or y_velocity == -self.__y_velocity):
            self.__x_velocity = x_velocity
            self.__y_velocity = y_velocity

    def update_position(self):
        '''Moves the snake in the direction it is facing'''

        #Each segment follows the previous segment
        for i in range(len(self)-1, 0, -1):
            self.__segments[i] = self.__segments[i-1]

        #Move the head last
        self.__segments[0] = self.__segments[0][0] + self.__x_velocity,\
                             self.__segments[0][1] + self.__y_velocity

    def __len__(self):
        return len(self.__segments)
