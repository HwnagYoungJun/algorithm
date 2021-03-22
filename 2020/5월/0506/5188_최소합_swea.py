import sys
sys.stdin = open('5188.txt')

dr = [0, 1]
dc = [1, 0]

def dfs(r, c, hap):
    global min_hap
    if hap >= min_hap:
        return
    elif (r, c) == (N - 1, N - 1):
        if min_hap > hap:
            min_hap = hap
            return
    for w in range(2):
        nr = r + dr[w]
        nc = c + dc[w]
        if 0 <= nc < N and 0 <= nr < N:
            dfs(nr, nc, hap + grim[nr][nc])

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    grim = [list(map(int, input().split())) for _ in range(N)]
    min_hap = float('inf')
    dfs(0, 0, grim[0][0])

    print("#{} {}".format(test_case, min_hap))

     