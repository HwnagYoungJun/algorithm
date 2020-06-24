import sys
from pprint import pprint
sys.stdin = open('19236.txt')
import copy

dr = ['no', -1, -1, 0, 1, 1, 1, 0, -1]
dc = ['no', 0, -1, -1, -1, 0, 1, 1, 1]

def dfs(eat_fish, m, f):
    global max_fish
    max_fish = max(max_fish, eat_fish)
    for fish_num, temp in f.items():
        if fish_num == 's':
            continue
        if temp == 'die':
            continue
        row, col = temp[0]
        d = temp[1]
        cnt = -1
        while cnt < 8:
            cnt += 1
            nr = row + dr[d]
            nc = col + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:

                if m[nr][nc] == 0:
                    f[fish_num] = [[nr, nc], d]
                    m[nr][nc], m[row][col] = m[row][col], m[nr][nc]
                    m[nr][nc][1] = d
                    break
                elif m[nr][nc][0] != 's':
                    f[fish_num][0], f[m[nr][nc][0]][0] = f[m[nr][nc][0]][0], f[fish_num][0]
                    m[nr][nc], m[row][col] = m[row][col], m[nr][nc]
                    f[fish_num][1] = d
                    m[nr][nc][1] = d
                    break
            
            if d == 8:
                d = 1
            else:
                d += 1

    pos, d = f['s']
    r, c = pos

    for w in range(1, 4):
        nr = r + dr[d] * w
        nc = c + dc[d] * w

        if 0 <= nr < 4 and 0 <= nc < 4:
            if m[nr][nc] == 0:
                continue
            copy_m = copy.deepcopy(m)
            copy_f = copy.deepcopy(f)
            pray_fish = copy_m[nr][nc]
            copy_f[pray_fish[0]] = 'die'
            copy_f['s'] = [[nr, nc], pray_fish[1]]
            copy_m[nr][nc] = ['s', pray_fish[1]]
            copy_m[r][c] = 0
            dfs(eat_fish + pray_fish[0], copy_m, copy_f)

fish = {i: ['pos', 'direction'] for i in range(1, 17)}
map_list = [[0 for _ in range(4)] for _ in range(4)]


for row in range(4):
    temp = list(map(int, input().split()))
    for col in range(4):
        map_list[row][col] = [temp[col * 2], temp[col * 2 + 1]]
        fish[temp[col * 2]] = [[row, col], temp[col * 2 + 1]]


first_pray = map_list[0][0][0]
fish[first_pray] = 'die'
map_list[0][0][0] = 's'
fish['s'] = [[0, 0], map_list[0][0][1]]
max_fish = float('-inf')
dfs(first_pray, map_list, fish)

print(max_fish)