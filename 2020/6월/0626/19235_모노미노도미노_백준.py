import sys
sys.stdin = open('19235.txt')

def Blue(t, r, c):

    if t == 1:
        for col in range(6):
            if blue[r][col] != 0:
                blue[r][col - 1] = t
                break
        else:
            blue[r][5] = t

    elif t == 2:
        for col in range(6):
            if blue[r][col] != 0:
                blue[r][col - 1] = t
                blue[r][col - 2] = t
                break
        else:
            blue[r][5] = t
            blue[r][4] = t

    else:
        for col in range(6):
            if blue[r][col] != 0 or blue[r + 1][col] != 0:
                blue[r][col - 1] = t
                blue[r + 1][col - 1] = t
                break
        else:
            blue[r][5] = t
            blue[r + 1][5] = t        


def Green(t, r, c):

    if t == 1:
        for row in range(6):
            if green[row][c] != 0:
                green[row - 1][c] = t
                break
        else:
            green[5][c] = t

    elif t == 2:
        for row in range(6):
            if green[row][c] != 0 or green[row][c + 1] != 0:
                green[row - 1][c] = t
                green[row - 1][c + 1] = t
                break
        else:
            green[5][c] = t
            green[5][c + 1] = t
    
    else:
        for row in range(6):
            if green[row][c] != 0:
                green[row - 1][c] = t
                green[row - 2][c] = t
                break
        else:
            green[5][c] = t
            green[4][c] = t


def blue_boom():

    global blue
    global score

    a = True
    while a:
        a = False
        for col in range(2, 6):
            for row in range(4):
                if blue[row][col] == 0:
                    break
            else:
                a = True
                score += 1
                for i in range(4):
                    blue[i] = [0] + blue[i][:col] + blue[i][col + 1:]

        if a:
            for col in range(4, -1, -1):
                for row in range(4):
                    if blue[row][col] == 0:
                        continue
                    if blue[row][col] == 3:
                        if row == 3:
                            continue
                        for c in range(col + 1, 6):
                            if blue[row][c] != 0 or blue[row + 1][c] != 0:
                                blue[row][c - 1], blue[row][col] = blue[row][col], blue[row][c - 1]
                                blue[row + 1][c - 1], blue[row + 1][col] = blue[row + 1][col], blue[row + 1][c - 1]

                                break
                        else:
                            blue[row][5] = blue[row][col]
                            blue[row + 1][5] = blue[row + 1][col]
                            blue[row][col] = 0
                            blue[row + 1][col] = 0
                    else:
                        for c in range(col + 1, 6):
                            if blue[row][c] != 0:
                                blue[row][c - 1], blue[row][col] = blue[row][col], blue[row][c - 1]
                                break
                        else:
                            blue[row][5] = blue[row][col]
                            blue[row][col] = 0
    chk = 0
    for i in range(4):
        if blue[i][0] != 0: 
            chk += 1
            break

    for i in range(4):
        if blue[i][1] != 0: 
            chk += 1
            break  
    
    if chk == 0:
        pass
    elif chk == 1:
        for i in range(4):
            blue[i] = [0] + blue[i][:5]
    else:
        for i in range(4):
            blue[i] = [0, 0] + blue[i][:4]


def green_boom():

    global green
    global score

    a = True

    while a:
        a = False
        for row in range(2, 6):
            for col in range(4):
                if green[row][col] == 0:
                    break
            else:
                a = True
                score += 1
                green = [[0, 0, 0 ,0]] + green[:row] + green[row + 1:]

        if a:
            for row in range(4, -1, -1):
                for col in range(4):
                    if green[row][col] == 0:
                        continue
                    if green[row][col] == 2:
                        if col == 3:
                            continue
                        for r in range(row + 1, 6):
                            if green[r][col] != 0 or green[r][col + 1] != 0:
                                green[r - 1][col], green[row][col] = green[row][col], green[r - 1][col]
                                green[r - 1][col + 1], green[row][col + 1] = green[row][col + 1], green[r - 1][col + 1]
                                break
                        else:
                            green[5][col] = green[row][col]
                            green[5][col + 1] = green[row + 1][col]
                            green[row][col] = 0
                            green[row + 1][col] = 0
                    else:
                        for r in range(row + 1, 6):
                            if green[r][col] != 0:
                                green[r - 1][col], green[row][col] = green[row][col], green[r - 1][col]
                                break
                        else:
                            green[5][col] = green[row][col]
                            green[row][col] = 0                    
    chk = 0
    for i in range(2):
        if green[i] != [0, 0, 0, 0]:
            chk += 1
    if chk == 0:
        pass
    elif chk == 1:
        green = [[0, 0, 0 ,0]] + green[:5]
    else:
        green = [[0, 0, 0, 0], [0, 0, 0, 0]] + green[:4]


N = int(input())
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0

for _ in range(N):
    t, row, col = map(int, input().split())

    Blue(t, row, col)
    Green(t, row, col)
    # print('set')
    # for i in blue:
    #     print(*i)
    # print()
    # for j in green:
    #     print(*j)
    # print()
    blue_boom()
    green_boom()
    # print('boom')
    # for i in blue:
    #     print(*i)
    # print()
    # for j in green:
    #     print(*j)
    # print()
print(score)
result = 0
for row in range(4):
    for col in range(6):
        if blue[row][col] != 0:
            result += 1
for row in range(6):
    for col in range(4):
        if green[row][col] != 0:
            result += 1
print(result)