import random, time, pygame, sys
from pygame.locals import *

FPS = 25
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = ','

MOVESIDEWAYSFREQ = 0.15
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#Making RGB
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (0, 0, 0)
RED         = (155, 0, 0)
LIGHTRED    = (175, 20, 20)
GREEN       = (0, 155, 0)
LIGHTGREEN  = (20, 175, 20)
BLUE        = (0, 0, 155)
LIGHTBLUE   = (20, 20, 175)
YELLOW      = (155, 155, 0)
LIGHTYELLOW = (175, 175, 20)

BORDERCOLOR = BLUE
BGCOLOR = BLACK
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS =(BLUE, GREEN, RED, YELLOW)
LIGHTCOLORS =(LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS)

TEMPLATEWIDTH  = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..00.',
                     '.00..',
                     '.....'],
                     ['.....',
                      '..0..',
                      '..00.',
                      '...0.',
                      '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.00..',
                     '..00.',
                     '.....'],
                     ['.....',
                      '..0..',
                      '.00..',
                      '.0...',
                      '.....']]

I_SHAPE_TEMPLATE = [['..0..',
                    '..0..',
                    '..0..',
                    '..0..',
                    '.....'],
                    ['.....',
                     '.....',
                     '0000.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.00..',
                     '.00..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
                     '.0...',
                     '.000.',
                     '.....',
                     '.....'],
                     ['.....',
                      '..00.',
                      '..0..',
                      '..0..',
                      '.....'],
                      ['.....',
                       '.000.',
                       '...0.',
                       '.....'],
                       ['.....',
                        '..0..',
                        '..0..',
                        '.00..',
                        '.....']]

L_SHAPE_TEMPLATE = [['.....',
                     '...0.',
                     '.000.',
                     '.....',
                     '.....'],
                     ['.....',
                      '..0..',
                      '..0..',
                      '..00.'],
                      ['.....',
                       '.....',
                       '.000.',
                       '.0...',
                       '.....'],
                       ['.....',
                        '.00..',
                        '..0..',
                        '..0..',
                        '.....']]

T_SHAPE_TEMPLATE = 