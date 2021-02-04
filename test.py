import math
import os
import random
import sys

import cfg
import pygame
import time

from snake import SnakeSprite

screen = pygame.display.set_mode((640, 480))
snake_pic = pygame.image.load(cfg.IMAGE_PATHS['sk'])
food_pic = pygame.image.load(cfg.IMAGE_PATHS['type'])
running = True

def main():
    clock = pygame.time.Clock()
    game_image = {}
    for key, value in cfg.IMAGE_PATHS.items():
        game_image[key] = pygame.image.load(value)

    food_X = random.randint(food_pic.get_rect().width, cfg.SCREENSIZE[0])
    food_Y = random.randint(food_pic.get_rect().height, cfg.SCREENSIZE[1])

    snake = SnakeSprite(snake_pic, (50, 50))

    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0] // game_image['newgrass'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_image['newgrass'].get_width() + 1):
                screen.blit(game_image['newgrass'], (x * 100, y * 100))

        screen.blit(food_pic, (food_X, food_Y))

        snake_speed = snake_pic.get_rect().width
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
            snake.snake_move('right', snake_speed)
        elif pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
            snake.snake_move('left', snake_speed)
        elif pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
            snake.snake_move('up', snake_speed)
        elif pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
            snake.snake_move('down', snake_speed)

        if (abs(snake.rect.left - food_X) < snake_pic.get_rect().width) and (
                snake_pic.get_rect().height > abs(snake.rect.top - food_Y)):
            food_X = random.randint(food_pic.get_rect().width, cfg.SCREENSIZE[0])
            food_Y = random.randint(food_pic.get_rect().height, cfg.SCREENSIZE[1])
            snake.snake_grow()

        snake.draw_snake(screen)
        pygame.display.flip()
        clock.tick(cfg.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(cfg.FPS)


if __name__ == '__main__':
    main()
