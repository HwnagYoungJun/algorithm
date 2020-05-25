import sys
sys.stdin = open('단지번호붙히기.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    deq = collections.deque()
    deq.append((r, c))
    count = 0
    while deq:
        row, col= deq.popleft()
        count += 1
        for w in range(4):

            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if dangi[nr][nc] == 1:
                    dangi[nr][nc] = 0
                    deq.append((nr, nc))
    return count


N = int(input())

dangi = [list(map(int, input())) for _ in range(N)]
result = list()
dangi_count = 0
for row in range(N):
    for col in range(N):
        if dangi[row][col] == 1:
            dangi[row][col] = 0
            result.append(bfs(row, col))
            dangi_count += 1

dangi.sort()
print(dangi_count)
for i in result:
    print(i)