import pygame
import cfg


class SnakeBlock(pygame.sprite.Sprite):
    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.position = position

    def move(self, direction, speed):
        if direction == 'right':
            self.rect.left = min(cfg.SCREENSIZE[0], self.rect.left + speed)
        elif direction == 'left':
            self.rect.left = max(0, self.rect.left - speed)
        elif direction == 'up':
            self.rect.top = max(0, self.rect.top - speed)
        elif direction == 'down':
            self.rect.top = min(cfg.SCREENSIZE[1], self.rect.top + speed)
        self.position = self.rect.left, self.rect.top


class SnakeSprite(pygame.sprite.Sprite):
    snake_block_array = {}

    def __init__(self, image, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.length = 1
        self.snake_block_array = {1: SnakeBlock(image, position)}
        self.snake_addition = SnakeBlock(image, position)

    def snake_grow(self):
        if self.length < 20:
            self.length += 1
            self.snake_block_array[self.length] = SnakeBlock(self.image, self.snake_addition.position)

    def snake_move(self, direction, speed):
        self.snake_addition.position = self.snake_block_array[self.length].position
        self.snake_block_array[1].move(direction, speed)
        for k in range(len(self.snake_block_array.keys()), 1, - 1):
            self.snake_block_array[k].position = self.snake_block_array[k-1].position
        self.rect.left, self.rect.top = self.snake_block_array[1].position

    def draw_snake(self, screen):
        for k in range(1, len(self.snake_block_array.keys()) + 1, 1):
            screen.blit(self.snake_block_array[k].image, self.snake_block_array[k].position)
