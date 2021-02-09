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
            self.rect.left = self.rect.left + speed
        elif direction == 'left':
            self.rect.left = self.rect.left - speed
        elif direction == 'up':
            self.rect.top = self.rect.top - speed
        elif direction == 'down':
            self.rect.top = self.rect.top + speed
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
        self.fullblood = 10
        self.blood = self.fullblood

    def snake_grow(self):
        if self.length < 10:
            self.length += 1
            self.snake_block_array[self.length] = SnakeBlock(self.image, self.snake_addition.position)

    def snake_move(self, direction, speed):
        self.snake_addition.position = self.snake_block_array[self.length].position
        for k in range(len(self.snake_block_array.keys()), 1, - 1):
            self.snake_block_array[k].position = self.snake_block_array[k - 1].position
        self.snake_block_array[1].move(direction, speed)
        self.rect.left, self.rect.top = self.snake_block_array[1].position
        if (self.snake_block_array[1].rect.left < 0)\
                or (self.snake_block_array[1].rect.top < 0)\
                or (self.snake_block_array[1].rect.right > cfg.SCREENSIZE[0])\
                or (self.snake_block_array[1].rect.bottom > cfg.SCREENSIZE[1]):
            self.blood -= 10

    def draw_snake(self, screen):
        for k in range(self.length, 0, -1):
            screen.blit(self.snake_block_array[k].image, self.snake_block_array[k].position)
