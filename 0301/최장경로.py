import sys
sys.stdin = open('최장경로.txt')

def dfs(row, k):
    global flag
    visit[row] = 1
    for col in range(1, N + 1):
        if graph[row][col] == 1 and visit[col] == 0:
            dfs(col, k + 1)
    visit[row] = 0
    if k > flag:
        flag = k

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    flag = -1
    visit = [0 for _ in range(N + 1)]
    for row in range(1, N + 1):
        dfs(row, 1)
    
    print('#{} {}'.format(test_case, flag))