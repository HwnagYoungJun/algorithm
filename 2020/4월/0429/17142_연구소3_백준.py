import sys
sys.stdin = open('17142.txt')
import collections
from itertools import combinations
import copy

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(virus_perm):
    global visit
    deq = collections.deque()
    q_virus = 0
    for r, c in virus_perm:
        deq.append((r, c, 0))
        visit[r][c] = 1

    while deq:
        row, col, time = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == 0:
                    if lab[nr][nc] != 1:
                        visit[nr][nc] = time + 1
                        deq.append((nr, nc, time + 1))
                        q_virus += 1
    return q_virus

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus = list()
temp = list()
tv = [[0 for _ in range(N)] for _ in range(N)]
yes_virus = -M
no_virus = 0
for row in range(N):
    for col in range(N):
        if lab[row][col] == 2:
            virus.append((row, col))
            yes_virus += 1
            lab[row][col] = 'virus'
        elif lab[row][col] == 1:
            temp.append((row, col))
            tv[row][col] = 1
        else:
            no_virus += 1

min_time = float('inf')

for i in combinations(virus, M):
    visit = copy.deepcopy(tv)
    max_time = float('-inf')
    qv = bfs(i)
    # print(qv, yes_virus, no_virus)    
    if qv == no_virus + yes_virus:
        for row in range(N):
            for col in range(N):
                if lab[row][col] != 'virus' and lab[row][col] != 1:
                    max_time = max(max_time, visit[row][col])
        if max_time == float('-inf'):
            max_time = 0
        min_time = min(min_time, max_time)
if min_time == float('inf'):
    min_time = -1
print(min_time)