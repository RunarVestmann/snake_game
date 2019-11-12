'''File that contains all the constants used throughout the project'''

#Gameplay
TIME_BETWEEN_FRAMES = 100

#Colors (r, g, b)
BACKGROUND_COLOR = (0, 0, 0)
FOOD_COLOR = (160, 0, 0)
SNAKE_COLOR = (0, 255, 0)

#Font
FONT = None #None leads to default windows font
FONT_SIZE = 30

#End game text
END_GAME_TEXT = "Your snake reached length "
END_GAME_TEXT_COLOR = (210, 180, 100)
END_GAME_TEXT_POSITION = (200, 300)


#Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640

#Grid
CELL_SIZE = 16
CELL_DIMENSIONS = (CELL_SIZE, CELL_SIZE)
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE   #number of cells in width
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE #number of cells in height
