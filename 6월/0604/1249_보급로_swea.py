import sys
sys.stdin = open('1249.txt')
import heapq

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dijkstra():
    INF = float('inf')
    start = (0, 0)
    end = (N - 1, N - 1)
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dist[start[0]][start[1]] = 0
    pq = []
    pq.append((0, start))
    heapq.heapify(pq)
    while pq:
        _, this_pos = heapq.heappop(pq)
        for w in range(4):
            nr = this_pos[0] + dr[w]
            nc = this_pos[1] + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                via = dist[this_pos[0]][this_pos[1]] + map_list[nr][nc]
                if via < dist[nr][nc]:
                    dist[nr][nc] = via
                    heapq.heappush(pq, (via, (nr, nc)))
    return dist[end[0]][end[1]]
    
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    map_list = [list(map(int, input())) for _ in range(N)]
    result = dijkstra()
    print("#{} {}".format(test_case, result))