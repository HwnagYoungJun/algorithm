import sys
sys.stdin = open('14499.txt')


dr = [None, 0, 0, -1, 1]
dc = [None, 1, -1, 0, 0]

def roll_dice(dice):

    temp = dice[:]

    if w == 1:
        dice[4] = temp[1]
        dice[3] = temp[6]
        dice[1] = temp[3]
        dice[6] = temp[4]

    elif w == 2:
        dice[4] = temp[6]
        dice[3] = temp[1]
        dice[1] = temp[4]
        dice[6] = temp[3]

    elif w == 3:
        dice[1] = temp[5]
        dice[6] = temp[2]
        dice[2] = temp[1]
        dice[5] = temp[6]

    else:
        dice[1] = temp[2]
        dice[6] = temp[5]
        dice[2] = temp[6]
        dice[5] = temp[1]

    
N, M, x, y, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
command_list = list(map(int, input().split()))
dice = [0] * 7

for i in range(K):
    w = command_list[i]
    nr = x + dr[w]
    nc = y + dc[w]
    if nr < 0 or nc < 0 or nr >= N or nc >= M:
        continue
    
    roll_dice(dice)

    if map_list[nr][nc] == 0:
        map_list[nr][nc] = dice[6]

    else:
        dice[6] = map_list[nr][nc]
        map_list[nr][nc] = 0
    
    x = nr
    y = nc

    print(dice[1])