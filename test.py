import math
import os
import random
import sys

import cfg
import pygame
import time

from snake import SnakeSprite

screen = pygame.display.set_mode((640, 480))
bunny_pic = pygame.image.load(cfg.IMAGE_PATHS['sk'])
bad_pic = pygame.image.load(cfg.IMAGE_PATHS['type'])
running = True
bunnyX = 200
bunnyY = 200


def main():
    global bunnyY, bunnyX

    clock = pygame.time.Clock()
    game_image = {}
    for key, value in cfg.IMAGE_PATHS.items():
        game_image[key] = pygame.image.load(value)

    badX = random.randint(50, cfg.SCREENSIZE[0])
    badY = random.randint(50, cfg.SCREENSIZE[1])

    snake = SnakeSprite(bunny_pic, (50, 50))

    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0] // game_image['newgrass'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_image['newgrass'].get_width() + 1):
                screen.blit(game_image['newgrass'], (x * 100, y * 100))

        screen.blit(bad_pic, (badX, badY))

        snake_speed = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
            snake.snake_move('right', snake_speed)
        elif pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
            snake.snake_move('left', snake_speed)
        elif pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
            snake.snake_move('up', snake_speed)
        elif pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
            snake.snake_move('down', snake_speed)

        if (abs(snake.rect.left - badX) < 10) and (abs(snake.rect.top - badY) < 10):
            badX = random.randint(50, cfg.SCREENSIZE[0])
            badY = random.randint(50, cfg.SCREENSIZE[1])
            snake.snake_grow()

        snake.draw_snake(screen)
        pygame.display.flip()
        clock.tick(cfg.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # while running:
        #     screen.fill(0)
        #     for x in range(cfg.SCREENSIZE[0]//game_image['grass'].get_width()+1):
        #         for y in range(cfg.SCREENSIZE[1]//game_image['grass'].get_width()+1):
        #             screen.blit(game_image['grass'], (x*100, y*100))
        #     bunnyX = bunnyX + 5
        #     if bunnyX > cfg.SCREENSIZE[0] :
        #         bunnyX = 0
        #         bunnyY = bunnyY + bunny_pic.get_height()
        #         if bunnyY > cfg.SCREENSIZE[1]:
        #             bunnyX = 50
        #             bunnyY = 50
        #     screen.blit(bunny_pic, (bunnyX, bunnyY))
        #     screen.blit(bad_pic, (400, 400))
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()

        pygame.display.flip()
        clock.tick(cfg.FPS)


if __name__ == '__main__':
    main()
