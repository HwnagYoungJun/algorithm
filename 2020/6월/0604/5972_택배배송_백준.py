# 1. 터진다 dfs로 하면 메모리가, 재귀가

import sys
sys.stdin = open('5972.txt')
import heapq

def dijkstra():
    dist = {i: float('inf') for i in range(1, N + 1)}
    dist[1] = 0

    pq = []
    pq.append((0, 1))
    heapq.heapify(pq)

    while pq:
        _, pos = heapq.heappop(pq)

        for cost, next_pos in road[pos]:
            via = dist[pos] + cost

            if via < dist[next_pos]:
                dist[next_pos] = via
                heapq.heappush(pq, (via, next_pos))

    return dist[N]

N, M = map(int, input().split())
road = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    a, b, c = map(int, input().split())
    road[a].append((c, b))
    road[b].append((c, a))

min_cost = dijkstra()
print(min_cost)