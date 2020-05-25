import sys
sys.stdin = open('유기농 배추.txt')
import collections

def bfs(row, col):
    deq = collections.deque()
    deq.append((row, col))
    배추밭[row][col] = 0

    while deq:
        r, c = deq.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]

            if 0 <= nr < M and 0 <= nc < N:
                if 배추밭[nr][nc] == 1:
                    배추밭 [nr][nc] = 0
                    deq.append((nr, nc))
    
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

T = int(input())

for test_case in range(1, T + 1):
    M, N, K = map(int, input().split())

    배추밭 = [[0 for _ in range(N)] for _ in range(M)]
    
    for i in range(K):
        br, bc = map(int, input().split())
        배추밭[br][bc] = 1
    벌레의숫자 = 0
    for row in range(M):
        for col in range(N):
            if 배추밭[row][col] == 1:
                벌레의숫자 += 1
                bfs(row, col)

    print(벌레의숫자)