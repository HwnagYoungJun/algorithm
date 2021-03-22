import sys
sys.stdin = open('4963.txt')
import collections

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(r, c):
    global island
    deq = collections.deque()
    deq.append((r, c))
    island[r][c] = cnt + 1

    while deq:
        row, col = deq.popleft()

        for w in range(8):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C:
                if island[nr][nc] == 1:
                    island[nr][nc] = cnt + 1
                    deq.append((nr, nc))
    
    return
    
while True:
    C, R = map(int, input().split())
    
    if (R, C) == (0, 0):
        break

    island = [list(map(int, input().split())) for _ in range(R)]

    cnt = 0
    for row in range(R):
        for col in range(C):
            if island[row][col] == 1:
                cnt += 1
                bfs(row, col)
                
    print(cnt)


