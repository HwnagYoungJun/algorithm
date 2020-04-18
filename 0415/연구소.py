import sys
sys.stdin = open('연구소.txt')
import collections
import copy
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def build_wall(index_set, index, k):
    global max_safe

    if k == 3:

        for j in index_set:
            r, c = able_to_wall[j]
            lab[r][c] = 1

        cnt = bfs()
        if cnt == '?':
            for j in index_set:
                r, c = able_to_wall[j]
                lab[r][c] = 0
            return
        else:
            safe = length - cnt - 3

            if safe > max_safe:
                max_safe = safe

            for j in index_set:
                r, c = able_to_wall[j]
                lab[r][c] = 0
            return
    
    for i in range(index, length):
        if visit[i] == 0:
            visit[i] = 1
            build_wall(index_set | {i}, i, k + 1)
            visit[i] = 0

def bfs():
    visit = [[0 for _ in range(M)] for _ in range(N)]
    count = 0
    temp = copy.copy(deq)
    while temp:
        br, bc = temp.popleft()
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc] == 0 and lab[nr][nc] == 0:
                    if count + 1 > length - 3 - max_safe:
                        return '?'
                    else: 
                        visit[nr][nc] = 1
                        count += 1
                        temp.append((nr, nc))

    return count

N, M = map(int, input().split())

lab = [list(map(int ,input().split())) for _ in range(N)]

able_to_wall = list()

deq = collections.deque()
max_safe = float('-inf')
for row in range(N):
    for col in range(M):
        if lab[row][col] == 0:
            able_to_wall.append((row, col))
        elif lab[row][col] == 2:
            deq.append((row, col))

length = len(able_to_wall)

for i in range(length - 2):

    visit = [0 for _ in range(length)]
    visit[i] = 1
    build_wall({i}, i, 1)

print(max_safe)