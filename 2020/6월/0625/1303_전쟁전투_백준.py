import sys
sys.stdin = open('1303.txt')
import collections

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, color):
    deq = collections.deque()
    deq.append((r, c))
    visit[(r, c)] = True
    p = 0
    while deq:
        row, col = deq.popleft()
        p += 1
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < M and 0 <= nc < N:
                if not visit[(nr, nc)]:
                    if war[nr][nc] == color:
                        visit[(nr, nc)] = True
                        deq.append((nr, nc))

    return p ** 2

N, M = map(int, input().split())
war = [list(input()) for _ in range(M)]

our_forces = 0
enermy = 0
visit = {(row, col): False for row in range(M) for col in range(N)}
for row in range(M):
    for col in range(N):
        if not visit[(row, col)]:
            color = war[row][col]
            power = bfs(row, col, color)
            if color == 'W':
                our_forces += power
            else:
                enermy += power

print(our_forces, enermy)