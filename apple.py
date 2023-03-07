import pygame

class Apple:
    def __init__(self):
        self.x = 5
        self.y = 5

    def draw(self, surface):
        color = pygame.Color(255, 0, 0)
        rect = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(surface, color, rect)
