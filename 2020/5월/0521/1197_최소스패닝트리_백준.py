# 1. 크루스칼로 푼 문제, 프림으로도 풀어보자

import sys
sys.stdin = open('1197.txt')
import heapq

V, E = map(int, input().split())

# 1. 인접리스트로 인접한 노드 만들기
adjacent_edges = [[] for _ in range(V + 1)]
# 2. 시작은 어디든지 상관없다. (MST는 모든 노드가 연결되어있다고 가정하고 푸는것)
start = 1
for _ in range(E):
    A, B, C = map(int, input().split())
    adjacent_edges[A].append((C, A, B))
    adjacent_edges[B].append((C, B, A))
# 3. 방문노드 저장소 / visited로 해도 상관없을것같다.
connetion_node = set()
connetion_node.add(start)
# 4. 시작 한곳에서 간선시작
candidate_edge_list = adjacent_edges[start]
heapq.heapify(candidate_edge_list)

result = 0
while candidate_edge_list:
    weight, n1, n2 = heapq.heappop(candidate_edge_list)
    if n2 not in connetion_node:
        connetion_node.add(n2)
        result += weight
        for edge in adjacent_edges[n2]:
            if edge[2] not in connetion_node:
                heapq.heappush(candidate_edge_list, edge)

print(result)