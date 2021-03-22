import sys
import heapq
sys.stdin = open('10776.txt')
a = round()
def dijkstra():
    INF = float('inf')
    pq = []
    pq.append((0, 0, A)) # (시간, 지금까지 깎아진 정도, 섬)
    heapq.heapify(pq)
    dist = [[INF for _ in range(K + 1)] for _ in range(N + 1)]
    dist[A][K] = 0

    while pq:
        utime, ucut, this_island = heapq.heappop(pq)
        for time, next_island, cut in conject[this_island]:
            if ucut + cut >= K:
                continue
            via = utime + time
            if dist[next_island][ucut + cut] > via:
                dist[next_island][ucut + cut] = via
                heapq.heappush(pq, (via, ucut + cut, next_island))

    return min(dist[B])
          
K, N, M = map(int, input().split())

conject = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    i1, i2, t, h = map(int, input().split())
    conject[i1].append((t, i2, h)) # (시간, 이어져있는섬, 깍기는정도)
    conject[i2].append((t, i1, h))

A, B = map(int, input().split())

result = dijkstra()
if result == float('inf'):
    result = -1
print(result)