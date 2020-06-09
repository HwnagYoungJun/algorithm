import sys
sys.stdin = open('1445.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
INF = float('inf')

def bfs():
    deq = collections.deque()
    deq.append((start[0], start[1], 0, 0))
    visit = {(row, col): [INF, INF] for col in range(M) for row in range(N)}
    visit[start] = [0, 0]

    while deq:
        row, col, garbage, side_of_g = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                ng = garbage
                ns = side_of_g
                if forest[nr][nc] == 'g':
                    ng += 1
                elif forest[nr][nc] == 'sg':
                    ns += 1
                if ng < visit[(nr, nc)][0]:
                    visit[(nr, nc)] = [ng, ns]
                    deq.append((nr, nc, ng, ns))

                elif ng == visit[(nr, nc)][0]:
                    if ns < visit[(nr, nc)][1]:
                        visit[(nr, nc)][1] = ns
                        deq.append((nr, nc, ng, ns))

    return visit[end]

N, M = map(int, input().split())
forest = [list(input()) for _ in range(N)]

# S: start, F: flower, g: 쓰레기
# 1. forest를 돌면서 S, F, g를 찾아서 각각을 저장, 그리고 g는 인접한곳도 g로 만들어버린다.
garbage_list = []
for row in range(N):
    for col in range(M):
        if forest[row][col] == 'S':
            start = (row, col)
        elif forest[row][col] == 'F':
            end = (row, col)
        elif forest[row][col] == 'g':
            garbage_list.append((row, col))

for row, col in garbage_list:
    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if 0 <= nr < N and 0 <= nc < M:
            if forest[nr][nc] == 'F' or forest[nr][nc] == 'S' or forest[nr][nc] == 'g':
                continue
            forest[nr][nc] = 'sg'

# 2. 시작 지점부터 bfs
print(*bfs())