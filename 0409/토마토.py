import sys
sys.stdin = open('토마토.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    tomato = N * M
    ic_tomato = 0
    for r in range(N):
        for c in range(M):
            if box[r][c] == 1:
                deq.append((r, c, 0))
                ic_tomato += 1
            elif box[r][c] == -1:
                tomato -= 1
    if tomato == ic_tomato:
        return 0
    while deq:
        row, col, count = deq.popleft()
        for w in range(4):
            
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if box[nr][nc] == 0:
                    ic_tomato += 1
                    if ic_tomato == tomato:
                        return count + 1
                    else:
                        box[nr][nc] = 1
                        deq.append((nr, nc, count + 1))
                        
    return -1

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
print(bfs())
