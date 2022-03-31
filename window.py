import pygame
from pygame.constants import CONTROLLER_BUTTON_LEFTSTICK
from pygame.scrap import put
pygame.init()

class Window:
    def __init__(self, width = 10, height = 10, fps = 30, name = "TicTac"):
        self.WIN_WIDTH = width
        self.WIN_HEIGHT = height
        self.FPS = 30
        self.screen = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.clock = pygame.time.Clock()
    def render(self, feild_height):
        line_height = 4
        pygame.draw.line(self.screen, GREEN, (0, 1), (self.WIN_WIDTH, 1), line_height)
        pygame.draw.line(self.screen, GREEN, (0, self.WIN_HEIGHT - line_height + 1), (self.WIN_WIDTH, self.WIN_HEIGHT - line_height + 1), line_height)
        pygame.draw.line(self.screen, GREEN, (1, 0), (1, self.WIN_HEIGHT), line_height)
        pygame.draw.line(self.screen, GREEN, (self.WIN_WIDTH - line_height + 1, 0), (self.WIN_WIDTH - line_height + 1, self.WIN_HEIGHT - line_height), line_height)
        pygame.draw.line(self.screen, WHITE, (0, 500), (self.WIN_WIDTH - line_height + 1, 500), line_height)
        step = self.WIN_WIDTH // feild_height
        for i in range(1, feild_height):
            pygame.draw.line(self.screen, GREEN, (0, i * step), (self.WIN_WIDTH, i * step), line_height)
        # update_height = self.WIN_HEIGHT - line_height
        # free_area = self.WIN_HEIGHT - (line_height * feild_height)
        # one_free_area = free_area // feild_height
        # up_step = (self.WIN_HEIGHT - (line_height + one_free_area) * feild_height) // 2
        # down_step = up_step + 4
        # for i in range(feild_height + 1):
        #     print(up_step + i * (one_free_area +line_height))
        #     pygame.draw.line(self.screen, GREEN, (0, up_step + i * (one_free_area +line_height)), (self.WIN_WIDTH, up_step + i * (one_free_area +line_height)), line_height)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
window = Window(width=500, height=500)
while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    window.render(4)
    pygame.display.update()
    window.clock.tick(10)