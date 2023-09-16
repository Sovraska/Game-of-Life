import time

import pygame

from setup import (
    clock, setup_grid, FPS, screen, GREY, BLACK,
    WHITE, resolution, cols, rows,
    make_2d_array, RED
)


def count_neighbors(grid, x, y):
    """count value of 8 neighbors around spot"""
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + i + cols) % cols
            row = (y + j + rows) % rows

            sum += grid[col][row]

    sum -= grid[x][y]
    return sum


def draw_grid(grid):
    """draw grid"""
    for i in range(cols):
        for j in range(rows):
            x = i * resolution
            y = j * resolution
            if grid[i][j] == 1:
                pygame.draw.rect(
                    screen, BLACK, (
                        x, y,
                        resolution - 1, resolution - 1
                    )
                )
            else:
                pygame.draw.rect(  # low performance to refactor, this isn`t good
                    screen, WHITE, (
                        x, y,
                        resolution - 1, resolution - 1
                    )
                )


def place_point(grid, mouse_pos):
    """place point in mouse position"""
    if pygame.mouse.get_pressed()[0] != 0:
        m_x, m_y = int(mouse_pos[0] / resolution), int(mouse_pos[1] / resolution)
        grid[m_x][m_y] = 1
    return grid


if __name__ == '__main__':
    grid = setup_grid()

    pause_button = pygame.Rect(0, 0, 40, 40)
    running = True
    is_stopped = False
    button_color = GREY

    while running:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] != 0:
            if pause_button.collidepoint(mouse_pos):
                time.sleep(0.1)
                is_stopped = not is_stopped

        if is_stopped:
            button_color = RED
        else:
            button_color = GREY

        if is_stopped:  # pause statement
            for i in range(cols):
                for j in range(rows):
                    grid = place_point(grid, mouse_pos)
            draw_grid(grid)
            pygame.draw.rect(screen, button_color, (0, 0, 40, 40))
        else:
            draw_grid(grid)

            pygame.draw.rect(screen, button_color, (0, 0, 40, 40))

            next_generation = make_2d_array(cols, rows)

            for i in range(cols):
                for j in range(rows):
                    state = grid[i][j]
                    sum = 0
                    neighbors = count_neighbors(grid, i, j)

                    if state == 0 and neighbors == 3:
                        next_generation[i][j] = 1
                    elif state == 1 and (neighbors < 2 or neighbors > 3):
                        next_generation[i][j] = 0
                    else:
                        next_generation[i][j] = state

                    next_generation = place_point(next_generation, mouse_pos)

            grid = next_generation

        pygame.display.flip()
    pygame.quit()
