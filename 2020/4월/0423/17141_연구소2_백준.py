import sys
sys.stdin = open('17141.txt')
import collections
from itertools import combinations
import copy

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(virus_perm):
    global visit
    deq = collections.deque()
    for j in virus_perm:
        r, c, = j
        deq.append((r, c, 0))
        visit[r][c] = 1
    while deq:
        row, col, time = deq.popleft()
        if time >= min_time:
            return float('inf')
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    deq.append((nr, nc, time + 1))
    
    if visit == [[1 for _ in range(N)] for _ in range(N)]:
        return time
    else:
        return float('inf')

N, M = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(N)]

virus = list()
temp = list()
tv = [[0 for _ in range(N)] for _ in range(N)]

for row in range(N):
    for col in range(N):
        if lab[row][col] == 2:
            virus.append((row, col))
        if lab[row][col] == 1:
            temp.append((row, col))
            tv[row][col] = 1

min_time = float('inf')

for i in combinations(virus, M):
    visit = copy.deepcopy(tv)
    min_time = min(min_time, bfs(i))

if min_time == float('inf'):
    min_time = -1
print(min_time)


