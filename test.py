import os
import cfg
import pygame
import time

screen = pygame.display.set_mode((800, 600))
bunny_pic = pygame.image.load(cfg.IMAGE_PATHS['rabbit'])
bad_pic = pygame.image.load(cfg.IMAGE_PATHS['badguy'])
running = True
bunnyX = 200
bunnyY = 200

def main():
    screen.blit(bunny_pic, (bunnyX, bunnyY))
    screen.blit(bad_pic, (400, 400))
    pygame.display.update()

    while running:
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_a]:
            screen.blit(bunny_pic, max((bunnyX - 10), 0), bunnyY)
            pygame.display.update()

        elif pressed_key[pygame.K_q]:
            pygame.quit()

        time.sleep(0.05)

    #time.sleep(3)







if __name__ == '__main__':
    main()