import sys
sys.stdin = open('16137.txt')
import collections
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    deq.append((0, 0, 0, 0, 0))
    visit = [[[0,0] for _ in range(N)] for _ in range(N)]
    visit[0][0] = [1, 1]

    while deq:
        row, col, time, dari, second = deq.popleft()
        # print(row, col, time, dari, second)
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if nr == N - 1 and nc == N - 1:
                    return time + 1
                fi = field[nr][nc]
                
                if fi == 1:
                    if visit[nr][nc][dari] == 0:
                        visit[nr][nc][dari] = 1
                        deq.append((nr, nc, time + 1, dari, 0))
                elif fi >= 2:
                    if (time + 1) % fi == 0 and second == 0:
                        if visit[nr][nc][dari] == 0:
                            visit[nr][nc][dari] =1
                            deq.append((nr, nc, time + 1, dari, 1))
                    else:
                        if second == 0:
                            if visit[nr][nc][dari] == 0:
                                deq.append((row, col, time + 1, dari, 0))
    
    
    return float('inf')





N, M = map(int, input().split())
cliff = list()

field = [list(map(int, input().split())) for _ in range(N)]

for row in range(N):
    for col in range(N):
        if field[row][col] == 0:
            cliff.append((row, col))

deep_cliff = list()
if cliff:
    for i in cliff:
        r, c = i
        if r > 0 and c > 0:
            if field[r-1][c] == field[r][c-1] == 0:
                deep_cliff.append((r, c))
                continue
        if r > 0 and c < N - 1:
            if field[r-1][c] == field[r][c+1] == 0:
                deep_cliff.append((r, c))
                continue
        if r < N - 1 and c > 0:
            if field[r+1][c] == field[r][c-1] == 0:
                deep_cliff.append((r, c))
                continue
        if r < N - 1 and c < N -1:
            if field[r+1][c] == field[r][c+1] == 0:
                deep_cliff.append((r, c))
if deep_cliff:
    for i in deep_cliff:
        r, c = i
        field[r][c] = -1
        cliff.remove(i)
min_dis = float('inf')
min_dis = min(bfs(), min_dis)

for i in cliff:
    r, c = i
    field[r][c] = M
    re = bfs()
    min_dis = min(re, min_dis)
    field[r][c] = 0

print(min_dis)