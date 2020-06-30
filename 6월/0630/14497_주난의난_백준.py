import sys
sys.stdin = open('14497.txt')
import collections
import heapq

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    pq = [(0, x1, y1)]
    heapq.heapify(pq)
    visit = [[False for _ in range(M)] for _ in range(N)]
    visit[x1][y1] = True

    while pq:
        time, row, col = heapq.heappop(pq)
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if visit[nr][nc]:
                    continue
                
                if (nr, nc) == (x2, y2):
                    return time + 1

                visit[nr][nc] = True
                
                if map_list[nr][nc] == '0':
                    heapq.heappush(pq, (time, nr, nc))
                else:                    
                    map_list[nr][nc] = 0
                    heapq.heappush(pq, (time + 1, nr, nc))
        


N, M = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1
map_list = [list(input()) for _ in range(N)]

print(bfs())