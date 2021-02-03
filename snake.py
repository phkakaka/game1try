import pygame
import cfg

class snake_block(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.position = position

    def move(self, direction, speed):
        if direction == 'right':
            self.rect.left = max(cfg.SCREENSIZE[0], self.rect.left + speed)
        elif direction == 'left':
            self.rect.left = min(0, self.rect.left - speed)
        elif direction == 'up':
            self.rect.top = min(0, self.rect.top - speed)
        elif direction == 'down':
            self.rect.top = max(cfg.SCREENSIZE[1], self.rect.top + speed)


class SnakeSprite(pygame.sprite.Sprite):
    snake_block_array = {}

    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.length = 1
        self.snake_block_array = {0: snake_block(image, position)}

    def snake_grow(self):
        self.length = max(10, self.length+1)

    def snake_move(self, direction, speed):
        self.snake_block_array[0].move(direction, speed)
        for k in self.snake_block_array.keys() - 1:
            self.snake_block_array[k+1].position = self.snake_block_array[k].position

    def draw_snake(self, screen):
        for k in self.snake_block_array.keys():
            screen.blit(self.snake_block_array[k].image, self.snake_block_array[k].position)

            




