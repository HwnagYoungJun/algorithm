###메메모
import sys
sys.stdin = open('19236.txt')
import collections
import copy
# cw
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
# 4X4 map

def dfs(f):
    global max_fish
    global map_list
    global fish
    print('11111111')
    for i in map_list:
        print(*i)
    print('1111111')
    for fish_num, value in fish.items():

        if fish_num == 'shark':
            continue
        if value == 'die':
            continue
        go = False
        d = value[1]
        cnt = 0
        while not go:

            if cnt >= 8:
                break
            nr = value[0][0] + dr[d]
            nc = value[0][1] + dc[d]

            if 0 <= nr < 4 and 0 <= nc < 4:
                if map_list[nr][nc] == 0:
                    go = True
                    fish[fish_num] = [(nr, nc), d]
                    map_list[nr][nc], map_list[value[0][0]][value[0][1]] = map_list[value[0][0]][value[0][1]], map_list[nr][nc]
                    continue

                elif map_list[nr][nc][0] != 's':
                    go = True
                    fish[map_list[nr][nc][0]][0] = [value[0][0], value[0][1]]
                    map_list[nr][nc], map_list[value[0][0]][value[0][1]] = map_list[value[0][0]][value[0][1]], map_list[nr][nc]
                    map_list[nr][nc][1] = d
                    fish[fish_num] = [[nr, nc], d]
                    continue
            # ccw
            cnt += 1
            if d == 7:
                d = 0
            else:
                d += 1
    temp_map = copy.deepcopy(map_list)

    # 상어이동
    rowcol, shark_d = fish['shark']
    row, col = rowcol
    shark_go_home = True
    for i in map_list:
        print(*i)
    print(row, col, shark_d)
    for w in range(1, 4):
        nr = row + dr[shark_d] * w 
        nc = col + dc[shark_d] * w
        if 0 <= nr < 4 and 0 <= nc < 4:
            if map_list[nr][nc] != 0:
                shark_go_home = False
                pray_fish = map_list[nr][nc][0]
                map_list[nr][nc][0] = 's'
                map_list[row][col] = 0
                temp_fish = copy.deepcopy(fish)
                fish['shark'] = [(nr, nc), map_list[nr][nc][1]]
                fish[pray_fish] = 'die'
                
                dfs(f + pray_fish)
                fish = copy.deepcopy(temp_fish)              
                map_list = copy.deepcopy(temp_map)
                print()
                for i in map_list:
                    print(*i)
                print()
                
    if shark_go_home:
        print(f)
        max_fish = max(max_fish, f)
        return


# 물고기는 dict로 관리
fish = {i: ['(pos_r, pos,c)', 'direction'] for i in range(1, 17)}
map_list = [[0 for _ in range(4)] for _ in range(4)]

for row in range(4):
    temp = list(map(int, input().split()))
    for col in range(0, 8, 2):
        fish[temp[col]] = [(row, col // 2), temp[col + 1] - 1]
        map_list[row][col // 2] = [temp[col], temp[col + 1] - 1]

fish['shark'] = [(0, 0), map_list[0][0][1]]
fish[map_list[0][0][0]] = 'die'
map_list[0][0] = ['s', fish['shark'][1]]

max_fish = 0
dfs(0)
print(max_fish)
            

    
