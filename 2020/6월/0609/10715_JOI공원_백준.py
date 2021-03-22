import sys
sys.stdin = open('10715.txt')
import heapq

INF = float('inf')

def dijkstra():
    dist = [[INF, set(), i] for i in range(N + 1)] 
    dist[1] = [0, set(), 1]
    pq = []
    pq.append((0, 1)) # (cost, node)
    heapq.heapify(pq)
    while pq:
        _, this_node = heapq.heappop(pq)
        for i in range(len(conj[this_node])):
            next_node, cost = conj[this_node][i]
            via = cost + dist[this_node][0]
            dist[next_node][1].add((this_node, i))
            if via < dist[next_node][0]:
                dist[next_node][0] = via
                heapq.heappush(pq, (via, next_node))
    return dist
    
# N개의 광장, M개의 도로
N, M, C = map(int, input().split())
# 인접 리스트 생성
conj = {i: [] for i in range(1, N + 1)}
d_cost = 0
for i in range(M):
    A, B, D = map(int, input().split())
    d_cost += D
    conj[A].append((B, D))
    conj[B].append((A, D))

# dijkstra로 1을 기준으로한 dijk 리스트 생성
destroy_doro = {i: False for i in range(M)}
temp_dijk = sorted(dijkstra())
min_cost = INF
visit = {i: False for i in range(1, N + 1)}
for i in range(N):
    visit[temp_dijk[i][2]] = True
    for destination, index in temp_dijk[i][1]:
        if visit[destination]:
            d_cost -= conj[destination][index][1]
    # 최종비용 = (C * X이하의 자연수 ) + (남은 도로의 길이)
    total_cost = (C * temp_dijk[i][0]) + d_cost
    min_cost = min(total_cost, min_cost)

print(min_cost)