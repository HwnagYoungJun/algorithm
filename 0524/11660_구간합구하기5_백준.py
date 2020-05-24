import sys
sys.stdin = open('11660.txt')

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
nw_list = [[0 for _ in range(N)] for _ in range(N)]
nw_list[0][0] = map_list[0][0]

for i in range(1, N):
    nw_list[i][0] = nw_list[i - 1][0] + map_list[i][0]
    nw_list[0][i] = nw_list[0][i - 1] + map_list[0][i]

for row in range(1, N):
    for col in range(1, N):
        nw_list[row][col] = nw_list[row - 1][col] + nw_list[row][col - 1]  - nw_list[row - 1][col - 1]+ map_list[row][col]



for i in nw_list:
    print(*i)
for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    if r1 == 0 and c1 == 0:
        print(nw_list[r2][c2])
    elif r1 == 0:
        print(nw_list[r2][c2] - nw_list[r2][c1 - 1])
    elif c1 == 0:
        print(nw_list[r2][c2] - nw_list[r1 - 1][c2])
    else:
        print(nw_list[r2][c2] + nw_list[r1 - 1][c1 - 1] - nw_list[r1 - 1][c2] - nw_list[r2][c1 - 1])