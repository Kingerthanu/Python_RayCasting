import math
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
# Player Settings
player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 3
# Game Object Sizes
TILE = 100
# Ray Casting Settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAXDEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DISTANCE = NUM_RAYS / (2*math.tan(HALF_FOV))
Pro_COEFF = DISTANCE * TILE
SCALE = WIDTH // NUM_RAYS
