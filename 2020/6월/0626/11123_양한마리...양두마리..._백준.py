import sys
sys.stdin = open('11123.txt')
import collections

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    deq = collections.deque()
    deq.append((r, c))
    visit[(r, c)] = True 
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visit[(nr, nc)]:
                continue
            if sheep_map[nr][nc] == '#':
                visit[(nr, nc)] = True
                deq.append((nr, nc))


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sheep_map = [list(input()) for _ in range(N)]
    visit = {(row, col): False for row in range(N) for col in range(M)}
    swarm = 0
    for row in range(N):
        for col in range(M):
            if visit[(row, col)]:
                continue
            if sheep_map[row][col] != '#':
                continue
            bfs(row, col)
            swarm += 1
    print(swarm)