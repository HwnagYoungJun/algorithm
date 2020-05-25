import sys
sys.stdin = open('행렬찾기.txt')
def dfs_r(row, col):
    global cnt_row
    cnt_row += 1
    nr = row + 1
    if 0 <= nr < N:
        if chemi[nr][col] != 0:
            dfs_r(nr, col)
def dfs_c(row, col):
    global cnt_col
    cnt_col += 1
    nc = col + 1
    if 0 <= nc < N:
        if chemi[row][nc] != 0:
            dfs_c(row, nc)
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    chemi = [list(map(int, input().split())) for _ in range(N)]
    temp_list = list()
    result = list()
    cnt = 0
    for row in range(N):
        for col in range(N):
            if chemi[row][col] != 0:
                cnt += 1
                cnt_row = 0
                cnt_col = 0
                dfs_c(row, col)
                dfs_r(row, col)
                for rr in range(row, row + cnt_row):
                    for cc in range(col, col + cnt_col):
                        chemi[rr][cc] = 0
                size = cnt_col * cnt_row
                temp_list.append([size, cnt_row, cnt_col])
    temp_list = sorted(temp_list)
    print(temp_list)
    for row in range(cnt):
        result.append(temp_list[row][1])
        result.append(temp_list[row][2])
    print('#{} {}'.format(test_case, cnt), *result)
            
