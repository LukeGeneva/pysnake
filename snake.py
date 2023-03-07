import pygame

class Snake:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.update_time = 0

    def draw(self, surface):
        color = pygame.Color(0, 255, 0)
        rect = pygame.Rect(self.x, self.y, 10, 10)
        pygame.draw.rect(surface, color, rect)

    def update(self, game_time):
        time_passed = game_time - self.update_time
        if time_passed > 1000:
            self.x += 10
            self.update_time = game_time
