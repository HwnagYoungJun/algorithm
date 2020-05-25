# 1. 프림알고리즘 연습을 위해 구지 프림으로 구현
# 2. 우선순위 큐로 만듬
# 3. 모든 집은 연결되어있다고 가정했으므로 탐색할필요는 X
# <TIL>
# 1. 프림 알고리즘 구현법
# 2. 프림은 많고 빽빽할 수록 메리트를 가짐
# <궁금한점>
# 1. 어느정도가 되야 프림이 크루스칼에 비해 메리트를 가질까?

import sys
sys.stdin = open('6497.txt')
import heapq

while True:
    m, n = map(int, input().split())
    if (m, n) == (0, 0):
        break

    # 1. 인접리스트 만들기 (weight, node)
    adjacent = [[] for _ in range(m)]
    electric = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        # (weight, node)식으로 넣어줘야 힙큐파이할 때 가중치를 기준으로 heap이 만들어진다
        adjacent[x].append((z, y))
        adjacent[y].append((z, x))
        electric += z

    # 어차피 다 연결되어 있으므로 시작위치는 중요하지 않다.
    start = 0
    # 2. 방문노드
    # set형식으로 만들어서 in으로 확인해도 된다.
    visit = [0 for _ in range(m)]
    visit[start] = 1

    # 3. 시작노드에서 연결되어있는 간선들을 heapq에 넣는다.
    cadidate_edge = adjacent[start]
    heapq.heapify(cadidate_edge)

    run = 0
    # 4. 간선을 큐에서 전부 제거할 때 까지 연결을 반복한다.
    while cadidate_edge:
        weight, next_node = heapq.heappop(cadidate_edge)
        if visit[next_node] == 0:
            visit[next_node] = 1
            run += weight
            for edge in adjacent[next_node]:
                if visit[edge[1]] == 0:
                    heapq.heappush(cadidate_edge, edge)

    result = electric - run
    print(result)