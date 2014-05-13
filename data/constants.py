import pygame as pg

#COLORS

BLACK =  0, 0, 0
WHITE = 255, 255, 255

#GAME STATES
LEVEL1 = 'level1'
MAIN_MENU = 'main menu'

#LEVEL STATES
NORMAL = 'normal'

#Player states
STANDING = 'standing'
WALKING = 'walking'
FREE_FALL = 'free fall'

#PLAYER values
SLOWEST_FREQUENCY = 100
START_JUMP_VEL = -1020
GRAVITY = 2520
RUN_SPEED = 600
WALK_SPEED = 350

#FONTS
MAIN_FONT = 'DroidSans'

#Directions

RIGHT = 'right'
LEFT = 'left'

#CONTROLS

JUMP_BUTTON = pg.K_a
RUN_BUTTON = pg.K_s

#ITEM BOX STATE
BUMPED = 'bumped'
OPENED = 'opened'
BUMP_SPEED = -1000
BUMP_GRAVITY = 6000