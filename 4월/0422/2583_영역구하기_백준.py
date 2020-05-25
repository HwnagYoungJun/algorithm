import sys
sys.stdin = open('2583.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):

    deq = collections.deque()
    deq.append((r, c))
    cnt = 1
    while deq:
        row, col = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            
            if 0 <= nr < M and 0 <= nc < N: 
                if area[nr][nc] == 0:
                    area[nr][nc] += 1
                    cnt += 1
                    deq.append((nr, nc))

    return cnt

M, N, K = map(int, input().split())

area = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    lc, lr, rc, rr = map(int, input().split())
    lr = M - lr
    rr = M - rr

    for row in range(rr, lr):
        for col in range(lc, rc):
            if area[row][col] == 0:
                area[row][col] = 1

count_area = 0
result = list()

for row in range(M):
    for col in range(N):
        if area[row][col] == 0:
            area[row][col] = 1
            count_area += 1
            squre = bfs(row, col)
            result.append((squre))

print(count_area)
result.sort()
print(*result)