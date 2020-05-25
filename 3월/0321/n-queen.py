import sys
sys.stdin = open("n-queen.txt")
import copy

def dfs(r, c, took, pan_map):
    global count
    print(r, c, took)
    for i in range(N):  # 좌, 우, 대각선 체크
        pan_map[r][i] = 1
        pan_map[i][c] = 1
        if 0 <= r - i < N and 0 <= c - i < N: # 좌상
            pan_map[r - i][c - i] = 1
        if 0 <= r + i < N and 0 <= c + i < N:  # 우하
            pan_map[r + i][c + i] = 1
        if 0 <= r - i < N and 0 <= c + i < N: # 우상
            pan_map[r - i][c + i] = 1
        if 0 <= r + i < N and 0 <= c - i < N: # 좌하
            pan_map[r + i][c - i] = 1

    temp_pan = copy.deepcopy(pan_map)
    for col in range(N):
        if pan_map[r + 1][col] == 0:
            if took + 1 == N:
                count += 1
                return
            else:
                dfs(r + 1, col, took + 1, pan_map)
            pan_map = temp_pan

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    for col in range(N):
        pan = [[0 for _ in range(N)] for _ in range(N)]
        dfs(0, col, 1, pan)
    print("#{} {}".format(test_case, count))