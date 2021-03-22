import sys
sys.stdin = open('16918.txt')
import collections

dr = [-1, 1, 0, 0, 0]
dc = [0, 0, -1, 1, 0]

R, C, N = map(int, input().split())
map_list = [list(input()) for _ in range(R)]

game_over = False
if N == 1:
    game_over = True
elif N == 2:
    map_list = [['O' for _ in range(C)] for _ in range(R)]
    game_over = True


if not game_over:

    plant_bomb = []
    for row in range(R):
        for col in range(C):
            if map_list[row][col] == 'O':
                plant_bomb.append((row, col))
    map_list = [['O' for _ in range(C)] for _ in range(R)]

    for test_case in range(3, N + 1):
        
        if test_case % 2:
            splash = set()
            for row, col in plant_bomb:
                for w in range(5):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if 0 <= nr < R and 0 <= nc < C:
                        splash.add((nr, nc))

            for row, col in splash:
                map_list[row][col] = '.'

            plant_bomb = []
            for row in range(R):
                for col in range(C):
                    if map_list[row][col] == 'O':
                        plant_bomb.append((row, col))
                        
        else:
            map_list = [['O' for _ in range(C)] for _ in range(R)]


for row in range(R):
    for col in range(C):
        if col == C - 1:
            print(map_list[row][col])
        else:
            print(map_list[row][col], end='')