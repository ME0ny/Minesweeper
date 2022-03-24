import random
from typing import List

messages = {1: "out of range", 2: "pushed yet", -1: "bomb", 0: "Ok", 3: "Win"}

class Field:
    turn_on = 1
    turn_off = 0
    bomb_icon = -1
    free_icon = 0
    flag_icon = -1

    def __init__(self, width: int = 20, height: int = 20):
        self.feild = self.init_feild(width=width, height=height)
        self.feild_of_push = [[0 for i in range(width)] for i in range(height)]

    def init_feild(self, width, height) -> List[int]:
        feild = [[0 for i in range(width)]for i in range(height)]
        bomb_count = random.randint(max(width, height), max(width, height) * min(width, height) / 5)
        for _ in range(bomb_count):
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

    def push_flag(self, pos_x, pos_y) -> int:
        if pos_x >= len(self.feild[0]) or pos_y >= len(self.feild):
            return 1
        if self.feild_of_push[pos_y][pos_x] == Field.turn_on:
            return 2
        self.feild_of_push[pos_y][pos_x] = Field.flag_icon
        if self.check_win() == True:
            return 3
        return 0     
  
    def step(self, pos_x, pos_y) -> int:
        if pos_x >= len(self.feild[0]) or pos_y >= len(self.feild):
            return 1
        if self.feild_of_push[pos_y][pos_x] == Field.turn_on:
            return 2
        if self.feild[pos_y][pos_x] == Field.bomb_icon:
            return -1
        if self.feild[pos_y][pos_x] == Field.free_icon:
            self.floodFill(pos_x, pos_y)
        self.feild_of_push[pos_y][pos_x] = Field.turn_on
        return 0

    def floodFillUtil(self, pos_x, pos_y, prevC):
        if pos_x < 0 or pos_x >= len(self.feild[0]) or pos_y < 0 or\
            pos_y >= len(self.feild) or self.feild[pos_y][pos_x] != prevC or\
            self.feild_of_push[pos_y][pos_x] == 1:
            if not (pos_x < 0 or pos_x >= len(self.feild[0]) or pos_y < 0 or pos_y >= len(self.feild)):
                self.feild_of_push[pos_y][pos_x] = 1    
            return
        self.feild_of_push[pos_y][pos_x] = 1
        self.floodFillUtil(pos_x + 1, pos_y, prevC)
        self.floodFillUtil(pos_x - 1, pos_y, prevC)
        self.floodFillUtil(pos_x, pos_y + 1, prevC)
        self.floodFillUtil(pos_x, pos_y - 1, prevC)
        self.floodFillUtil(pos_x - 1, pos_y - 1, prevC)
        self.floodFillUtil(pos_x + 1, pos_y - 1, prevC)
        self.floodFillUtil(pos_x - 1, pos_y + 1, prevC)
        self.floodFillUtil(pos_x + 1, pos_y + 1, prevC)

    def floodFill(self, pos_x, pos_y):
        prevC = self.feild[pos_y][pos_x]
        self.floodFillUtil(pos_x, pos_y, prevC)

    def render(self):
        for i in range(len(self.feild)):
            for j in range(len(self.feild[0])):
                if self.feild_of_push[i][j] != Field.turn_on:
                    print("  ",end="")
                else:
                    print(self.feild[i][j], "",end="")
                print("|",end="")
            print()
            print(len(self.feild[0])*"---")

    def check_win(self) -> bool:
        for i in range(len(self.feild)):
            for j in range(len(self.feild[0])):
                if self.feild[i][j] == Field.bomb_icon:
                    if self.feild_of_push[i][j] != Field.flag_icon:
                        return False
        return True

if __name__ == "__main__":
    a = Field()
    while(True):
        print("FLAG:\t1 - step; 0 - flag")
        flag, pos_x, pos_y = [int(i) for i in input("flag, x, y:\t").split()]
        if flag == 1:
            status = a.step(pos_x, pos_y)
        if flag == 0:
            status = a.push_flag(pos_x, pos_y)
        if status == 0:
            a.render()
            continue
        print(messages[status])
        if status == -1:
            break
    
    