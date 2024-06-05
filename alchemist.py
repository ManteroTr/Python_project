import pygame
import random


class Alchemist(pygame.sprite.Sprite):

    def __init__(self, weight, height):
        super().__init__()
        self.weight = weight
        self.height = height
        self.image = pygame.transform.scale(pygame.image.load('image/alchemist.png').convert_alpha(), (150, 242))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(101, 1000)
        self.rect.y = random.randint(101, 558)

    def draw_alchemist(self, screen):
        screen.blit(self.image, self.rect)
