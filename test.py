import math
import os
import random
import sys
import cfg
import pygame
import time
from snake import SnakeSprite

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((cfg.SCREENSIZE[0], cfg.SCREENSIZE[1]))
    snake_pic = pygame.image.load(cfg.IMAGE_PATHS['train'])
    food_pic = pygame.image.load(cfg.IMAGE_PATHS['type'])
    bloodbar = pygame.image.load(cfg.IMAGE_PATHS['healthbar'])
    blood = pygame.image.load(cfg.IMAGE_PATHS['health'])
    font = pygame.font.Font(None, 30)
    running = True

    snake = SnakeSprite(snake_pic, (50, 50))

    clock = pygame.time.Clock()
    game_image = {}
    for key, value in cfg.IMAGE_PATHS.items():
        game_image[key] = pygame.image.load(value)

    foodx = random.randint(0, cfg.SCREENSIZE[0] - food_pic.get_rect().width)
    foody = random.randint(snake_pic.get_height(), cfg.SCREENSIZE[1] - food_pic.get_rect().height)

    while running:
        screen.fill(0)
        for x in range(cfg.SCREENSIZE[0] // game_image['ground'].get_width() + 1):
            for y in range(cfg.SCREENSIZE[1] // game_image['ground'].get_height() + 1):
                screen.blit(game_image['ground'], (x * 100, y * 100))

        sys_timer = pygame.time.get_ticks()
        timer_text = font.render(str(sys_timer // 60000).zfill(2) + ':'
                                 + str(sys_timer // 1000 % 60).zfill(2), True, (200, 0, 0))
        timer_rect = timer_text.get_rect()
        timer_rect.topleft= [cfg.SCREENSIZE[0] - 100, 5]
        screen.blit(timer_text, timer_rect)

        screen.blit(food_pic, (foodx, foody))

        snake_speed = snake_pic.get_rect().width
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
            if snake.rect.right < cfg.SCREENSIZE[0]:
                snake.snake_move('right', snake_speed)
            else:
                snake.blood -= 1
        elif pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
            if snake.rect.left > 0:
                snake.snake_move('left', snake_speed)
            else:
                snake.blood -= 1
        elif pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
            if snake.rect.top > snake.image.get_height():
                snake.snake_move('up', snake_speed)
            else:
                snake.blood -= 1
        elif pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
            if snake.rect.bottom < cfg.SCREENSIZE[1]:
                snake.snake_move('down', snake_speed)
            else:
                snake.blood -= 1

        if (abs(snake.rect.left - foodx) < snake_pic.get_rect().width) and (
                snake_pic.get_rect().height > abs(snake.rect.top - foody)):
            foodx = random.randint(0, cfg.SCREENSIZE[0] - food_pic.get_rect().width)
            foody = random.randint(snake_pic.get_height(), cfg.SCREENSIZE[1] - food_pic.get_rect().height)
            snake.snake_grow()

        screen.blit(bloodbar, [10, 5])
        for i in range((bloodbar.get_width() // blood.get_width() *
                        (snake.blood // snake.fullblood))):
            screen.blit(blood, (i + 10, 8))

        current_goal = snake.length
        current_goal_text = font.render(str(current_goal), True, (255, 0, 0))
        current_goal_rect = current_goal_text.get_rect()
        current_goal_rect.topleft = [(cfg.SCREENSIZE[0] // 2), 5]
        screen.blit(current_goal_text, current_goal_rect)

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
