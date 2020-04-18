import sys
sys.stdin = open('러시아 국기 같은 깃발.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split()) # N : row C: col
    flag_map = [list(input()) for _ in range(N)]
    min_paint = float('inf')
    for i in range(0, N - 2):
        temp_num = 0
        for ii in range(0, i + 1):
            for col_i in range(M):
                if flag_map[ii][col_i] != 'W':
                    temp_num += 1
        for j in range(i + 1, N - 1):
            count = temp_num
            for jj in range(i + 1, j + 1):
                for col_j in range(M):
                    if flag_map[jj][col_j] != 'B':
                        count += 1
            for k in range(j + 1, N):
                for col_k in range(M):
                    if flag_map[k][col_k] != 'R':
                        count += 1
            if min_paint > count:
                min_paint = count
    print("#{} {}".format(test_case, min_paint))
                
