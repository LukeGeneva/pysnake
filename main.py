import pygame
from pygame.locals import *
from apple import Apple
from snake import Snake
 
class Game:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 640, 400
        self.apple = Apple()
        self.snake = Snake()
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        self.snake.update(pygame.time.get_ticks())

    def on_render(self):
        pygame.draw.rect(self._display_surf, pygame.Color(0, 0, 0), pygame.Rect(0, 0, self.width, self.height))
        self.apple.draw(self._display_surf)
        self.snake.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    game = Game()
    game.on_execute()
