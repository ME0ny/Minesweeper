from turtle import width
import typing
import random
import pygame
from pygame.constants import CONTROLLER_BUTTON_LEFTSTICK
from pygame.scrap import put
pygame.init()

class Window:
    def __init__(self, width = 10, height = 10, fps = 30, name = "TicTac"):
        self.size_of_box = 50
        self.WIN_WIDTH = width * self.size_of_box
        self.WIN_HEIGHT = height * self.size_of_box
        self.FPS = 30
        self.screen = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))
        self.clock = pygame.time.Clock()
    def render_field(self, field_of_push, feild):
        for i in range(self.WIN_WIDTH // self.size_of_box + 1):
            pygame.draw.line(self.screen, WHITE, (0 + self.size_of_box * i,0), (0 + self.size_of_box * i, self.WIN_HEIGHT), 3)
        for i in range(self.WIN_HEIGHT // self.size_of_box + 1):
            pygame.draw.line(self.screen, WHITE, (0, 0 + self.size_of_box * i), (self.WIN_WIDTH, 0 + self.size_of_box * i), 3)
        for y in range(len(field)):
            for x in range(len(feild[0])):
                if field_of_push[y][x] == 1:
                    text = basic_font.render(str(field[y][x]), True, WHITE, BLACK)
                    text_pos = (self.size_of_box * x + self.size_of_box // 3, self.size_of_box * y + self.size_of_box // 5)
                    window.screen.blit(text, text_pos)
def init_feild(width: int = 20, height: int = 20):
    feild = [[0 for i in range(width)]for i in range(height)]
    bomb_count = random.randint(width * height // 20, width * height // 10)
    for i in range(bomb_count):
        while (True):
            bomb_x = random.randint(0, width-1)
            bomb_y = random.randint(0, height-1)
            if  feild[bomb_y][bomb_x] != -1:
                feild[bomb_y][bomb_x] = -1
                break
    for y in range(height):
        for x in range(width):
            if feild[y][x] == -1:
                continue
            count = 0
            if y - 1 >= 0 and x - 1 >= 0:
                if feild[y - 1][x - 1] == -1:
                    count += 1
            if y - 1 >= 0 and x >= 0:
                if feild[y - 1][x] == -1:
                    count += 1
            if y - 1 >= 0 and x + 1 < width:
                if feild[y - 1][x + 1] == -1:
                    count += 1
            if y >= 0 and x - 1 >= 0:
                if feild[y][x - 1] == -1:
                    count += 1
            if y >= 0 and x + 1 < width:
                if feild[y][x + 1] == -1:
                    count += 1
            if y + 1 < height and x - 1 >= 0:
                if feild[y + 1][x - 1] == -1:
                    count += 1
            if y + 1 < height and x >= 0:
                if feild[y + 1][x] == -1:
                    count += 1
            if y + 1 < height and x + 1 < width:
                if feild[y + 1][x + 1] == -1:
                    count += 1
            feild[y][x] = count
    return feild           

def find_all_zero():
    pass
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)
WIN_WIDTH = 500
WIN_HEIGHT = 500
FPS = 30
basic_font = pygame.font.SysFont(None, 48)
mouse_pos = [0, 0]
click_flag = False
width = 10
height = 10
field = init_feild(width=width, height=height)
field_of_push = [[0 for i in range(len(field[0]))]for i in range(len(field))]
window = Window(width=len(field[0]), height=len(field))
while (True):
    window.render_field(field_of_push, field)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN and click_flag == False:
            click_flag = True
        if event.type == pygame.MOUSEBUTTONUP:
            click_flag = False
    if click_flag:
        click_x = mouse_pos[0] // window.size_of_box
        clock_y = mouse_pos[1] // window.size_of_box
        field_of_push[mouse_pos[1] // window.size_of_box][mouse_pos[0] // window.size_of_box] = 1
        if field[clock_y][click_x] == 0:
            pass
    # конец прорисовки окна
    pygame.display.update()
    window.clock.tick(10)
if __name__ == '__main__':
    feild = init_feild()
    for i in feild:
        for j in i:
            print("\t", j, end="")
        print()