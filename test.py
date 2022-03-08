import typing
import random

def init_feild(width: int = 10, height: int = 10):
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
                
         
if __name__ == '__main__':
    feild = init_feild()
    for i in feild:
        for j in i:
            print("\t", j, end="")
        print()
