import random

import pygame

WIDTH = 1067
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (51, 51, 51)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.init()

pygame.display.set_caption("Game Of Life")
clock = pygame.time.Clock()
pygame.init()

pygame.font.init()

grid = None
resolution = 8
cols = WIDTH / resolution
rows = HEIGHT / resolution
cols = int(cols)
rows = int(rows)


def make_2d_array(cols, rows):
    """make empty array"""
    arr = [0] * cols
    for i in range(cols):
        arr[i] = [0] * rows
    return arr


def setup_grid():
    """can generate random field"""
    grid = make_2d_array(cols, rows)
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = random.randint(0, 0)
    return grid
