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
from modules import *


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
    # define bunny
    bunny = BunnySprite(image=game_image.get('rabbit'), position=(100, 100))
    acc_record = [0., 0.]
    healthvalue = 194
    arrow_sprites_group = pygame.sprite.Group()

    badguy_sprites_group = pygame.sprite.Group()
    badguy = BadguySprite(game_image.get('badguy'), position=(640, 100))
    badguy_sprites_group.add(badguy)

    badtimer = 100
    badtimer1 = 0

    running, exitcode = True, False
    clock = pygame.time.Clock()

    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0]//game_image['grass'].get_width()+1):
            for y in range(cfg.SCREENSIZE[1]//game_image['grass'].get_height()+1):
                screen.blit(game_image['grass'], (x*100, y*100))
        for i in range(4):screen.blit(game_image['castle'], (0, 30+105*i))

        countdown_text = font.render(str((90000-pygame.time.get_ticks())//60000)+":"+str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0, 0, 0))
        countdown_rect = countdown_text.get_rect()
        countdown_rect.topright = [635, 5]
        screen.blit(countdown_text, countdown_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_sounds['shoot'].play()
                acc_record[1] += 1
                mouse_pos = pygame.mouse.get_pos()
                angle = math.atan2(mouse_pos[1]-(bunny.rotated_position[1]+32), mouse_pos[0]-(bunny.rotated_position[0]+26))
                arrow = ArrowSprite(game_image.get('arrow'), (angle, bunny.rotated_position[0]+32, bunny.rotated_position[1]+26))
                arrow_sprites_group.add(arrow)

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            bunny.move(cfg.SCREENSIZE, 'up')
        elif key_pressed[pygame.K_s]:
            bunny.move(cfg.SCREENSIZE, 'down')
        elif key_pressed[pygame.K_a]:
            bunny.move(cfg.SCREENSIZE, 'left')
        elif key_pressed[pygame.K_d]:
            bunny.move(cfg.SCREENSIZE, 'right')

        for arrow in arrow_sprites_group:
            if arrow.update(cfg.SCREENSIZE):
                arrow_sprites_group.remove(arrow)

        if badtimer == 0:
            badguy = BadguySprite(game_image.get('badguy'), position=(640, random.randint(50, 430)))
            badguy_sprites_group.add(badguy)
            badtimer = 100 - (badtimer1 * 2)
            badtimer1 = 20 if badtimer1>=20 else badtimer1+2
        badtimer -= 1
        for badguy in badguy_sprites_group:
            if badguy.update():
                game_sounds['hit'].play()
                healthvalue -= random.randint(4, 8)
                badguy_sprites_group.remove(badguy)

        for arrow in arrow_sprites_group:
            for badguy in badguy_sprites_group:
                if pygame.sprite.collide_mask(arrow, badguy):
                    game_sounds['enemy'].play()
                    arrow_sprites_group.remove(arrow)
                    badguy_sprites_group.remove(badguy)
                    acc_record[0] += 1

        arrow_sprites_group.draw(screen)
        badguy_sprites_group.draw(screen)
        bunny.draw(screen, pygame.mouse.get_pos())

        screen.blit(game_image.get('healthbar'), (5, 5))
        for i in range(healthvalue):
            screen.blit(game_image.get('health'), (i+8, 8))

        if pygame.time.get_ticks() >= 90000:
            running, exitcode = False, True
        if healthvalue <= 0:
            running, exitcode = False, True

        pygame.display.flip()
        accuracy = acc_record[0] / acc_record[1] * 100 if acc_record[1] > 0 else 0
        accuracy = '%.2f' % accuracy
        showEndGameInterface(screen, exitcode, accuracy, game_image)


'''run'''
if __name__ == '__main__':
    main()





























