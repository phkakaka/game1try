'''
function:
    Bunnies and Badgers
author:
    Samuel.wang
'''

import sys
import cfg
import math
import random
import pygame

'''initial the game'''
def initGame():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('bunnies and badgers -- Samuel')

    game_images = {}
    for key, value in cfg.IMAGE_PATHS.items():
        game_images[key] = pygame.image.load(value)

    game_sounds = {}
    for key, value in cfg.SOUNDS_PATHS.items():
        if key != 'moonlight':
            game_sounds[key] = pygame.mixer.Sound(value)

    return screen, game_images, game_sounds


def main():
    screen, game_image, game_sounds = initGame()

    pygame.mixer.music.load(cfg.SOUNDS_PATHS['moonlight'])
    pygame.mixer.music.play(-1, 0.0)
    font = pygame.font.Font(None, 24)

'''run'''
if __name__ == '__main__':
    main()