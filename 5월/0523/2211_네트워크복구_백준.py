# 1. 최소 개수의 회선만을 복구해야 된다 => N-1개만 살려서 최소 신장트리를 만들어야된다
# 2. 슈퍼컴퓨터에서 가는 거리가 최소여야하므로 다익스트라로 구현
# 3. 다익스트라를 써야하므로 구조가 비슷한 프림을 쓸 예정
# <풀고나서느낀점>
# 1. MST는 함정이다.

import sys
sys.stdin = open('2211.txt')
import heapq

def dijkstra(grape):
    dist = [float('inf') for _ in range(N + 1)]
    dist[1] = 0
    visit = {i: False for i in range(N + 1)}
    pq = []
    pq.append((0, 1, -1))
    heapq.heapify(pq)
    K = 0
    recovery_list = []
    while pq:
        _, this_node, priv_node = heapq.heappop(pq)
        if visit[this_node]:
            continue
        if priv_node != -1:
            recovery_list.append((priv_node, this_node))
            K += 1
        visit[this_node] = True
        for cost, next_node in grape[this_node]:
            via = cost + dist[this_node]
            if via < dist[next_node]:
                dist[next_node] = via
                heapq.heappush(pq, (via, next_node, this_node))
    
    return K, recovery_list

        
N, M = map(int, input().split())

adj = {i: [] for i in range(N + 1)}

for _ in range(M):
    c1, c2, weight = map(int, input().split())
    adj[c1].append((weight, c2))
    adj[c2].append((weight, c1))

K, recover = dijkstra(adj)

print(K)

for i in recover:
    print(*i)