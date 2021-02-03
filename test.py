import math
import os
import random

import cfg
import pygame
import time

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

    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0] // game_image['newgrass'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_image['newgrass'].get_width() + 1):
                screen.blit(game_image['newgrass'], (x * 100, y * 100))

        screen.blit(bad_pic, (badX, badY))

        bunny_speed = 5
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
            bunnyX = bunnyX + bunny_speed
        elif pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
            bunnyX = bunnyX - bunny_speed
        elif pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
            bunnyY = bunnyY - bunny_speed
        elif pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
            bunnyY = bunnyY + bunny_speed
        if bunnyX > cfg.SCREENSIZE[0]:
            bunnyX = 0
        elif bunnyX <= 0:
            bunnyX = cfg.SCREENSIZE[0]
        if bunnyY > cfg.SCREENSIZE[1]:
            bunnyY = 0
        elif bunnyY <= 0:
            bunnyY = cfg.SCREENSIZE[1]

        if (abs(bunnyX - badX) < 5) and (abs(bunnyY - badY) < 5):
            badX = random.randint(50, cfg.SCREENSIZE[0])
            badY = random.randint(50, cfg.SCREENSIZE[1])

        screen.blit(bunny_pic, (bunnyX, bunnyY))
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
