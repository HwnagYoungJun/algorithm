import sys
sys.stdin = open('2589.txt')
import collections
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def bfs(r, c):
    global temp
    deq = collections.deque()
    deq.append((r, c, 0))
    visit = [[0 for _ in range(C)] for _ in range(R)]
    visit[r][c] = 1

    while deq:
        row, col, time = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < R and 0 <= nc < C:
                if visit[nr][nc] == 0 and island[nr][nc] == 'L':
                    visit[nr][nc] = 1
                    deq.append((nr, nc, time + 1))

    temp[r][c] = time
    return
R, C = map(int, input().split())

island = [list(input()) for _ in range(R)]
temp = [[0 for _ in range(C)] for _ in range(R)]
for row in range(R):
    for col in range(C):
        if island[row][col] == 'L':
            bfs(row, col)
result = float('-inf')
for i in temp:
    result = max(result, max(i))
print(result)
    