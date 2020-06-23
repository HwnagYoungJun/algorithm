import sys
sys.setrecursionlimit(2500)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find(r, c):
    global temp_set
    for w in range(4):
        nr = r + dr[w]
        nc = c + dc[w]
        if 1 <= nr < N + 1 and -1 <= nc <= M:
            if nc == M:
                nc = 0
            elif nc == -1:
                nc = M - 1
            if visit[nr][nc]:
                continue
            if stencil[r][c] == stencil[nr][nc]:
                temp_set.add((nr, nc))
                visit[nr][nc] = True
                find(nr, nc)


# N개의 원판, M개의 숫자, T개의 돌림
N, M, T = map(int, input().split())

stencil = dict()

for i in range(1, N + 1):
    stencil[i] = list(map(int, input().split()))

for test_case in range(T):
    # x의 배수 원판, d 방향으로(0 cw, 1 ccw), K번 회전
    x, d, k = map(int, input().split())
    k = k % M
    possible_row = []

    for n in range(x, N + 1):
        if n % x == 0:
            possible_row.append(n)
    # cw
    if d == 0:
        # 돌려돌려돌림판
        for i in possible_row:
            stencil[i] = stencil[i][(M - k):] + stencil[i][:(M - k)]  
            
    # ccw
    else:
        for i in possible_row:
            stencil[i] = stencil[i][k:] + stencil[i][:k] 
    # print(possible_row)
    # print(stencil)
    # 인접한곳을 보아라
    visit = [[False for _ in range(M)] for _ in range(N + 1)]
    temp_set = set()
    total_num = 0
    cnt = 0
    for row in range(1, N + 1):
        for col in range(M):
            total_num += stencil[row][col]
            if stencil[row][col] != 0:
                cnt += 1
                if not visit[row][col]:
                    find(row, col)        
    for r, c in temp_set:
        stencil[r][c] = 0

    # 하나도 바뀌지 않았다면
    if temp_set == set():
        if cnt == 0:
            avg_total = 0
        else:
            avg_total = total_num / cnt
            for row in range(1, N + 1):
                for col in range(M):
                    if stencil[row][col] == 0:
                        continue
                    if stencil[row][col] > avg_total:
                        stencil[row][col] -= 1
                    elif stencil[row][col] < avg_total:
                        stencil[row][col] += 1

    if test_case == T - 1:
        result = 0
        for row in range(1, N + 1):
            for col in range(M):
                result += stencil[row][col]

print(result)