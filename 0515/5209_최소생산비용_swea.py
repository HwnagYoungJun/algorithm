import sys
sys.stdin = open('5209.txt')

def dfs(r, c, cost):
    global min_cost

    if cost >= min_cost:
        return
    if r == N - 1:
        min_cost = cost
        return
    
    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            dfs(r + 1, i, cost + factory[r + 1][i])
            visit[i] = 0


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())

    factory = [list(map(int, input().split())) for _ in range(N)]
    min_cost = float('inf')
    visit = [0 for _ in range(N)]

    for i in range(N):
        visit[i] = 1
        dfs(0, i, factory[0][i])
        visit[i] = 0
        print(visit)
        
    print("#{} {}".format(test_case, min_cost))