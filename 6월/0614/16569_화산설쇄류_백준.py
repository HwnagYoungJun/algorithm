import sys
sys.stdin = open('16559.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    deq.append((X, Y))
    visit = {(r, c): False for r in range(M) for c in range(N)}
    vol_visit = {(r, c): False for r in range(M) for c in range(N)}
    for i in volcano:
        vol_visit[(i[0], i[1])] = True
    visit[(X, Y)] = True
    max_height = float('-inf')
    just_like_that_time = -1
    time = 0
    while deq:
        # 화산 폭발!
        for this_volcano in volcano:
            if this_volcano[2] < time:
                continue
            for w in range(4):
                nr = volcano[0] + dr[w]
                nc = volcano[1] + dc[w]
                if 0 <= nr < M and 0 <= nc < N:
                    if vol_visit[(nr, nc)]:
                        continue
                    vol_visit[(nr, nc)] = True
                    volcano.append((nr, nc, this_volcano[2]))

        for _ in range(len(deq)):
            row, col, time = deq.popleft()


        

# M: row, N: col
M, N, V = map(int, input().split())
X, Y = map(int, input().split())
X -= 1
Y -= 1
godo = [list(map(int, input().split())) for _ in range(M)]
volcano = collections.deque()
for _ in range(V):
    x, y, t = map(int, input().split())
    volcano.append((x - 1, y - 1, t))



