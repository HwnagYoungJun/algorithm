import sys
sys.stdin = open('5251.txt')

# 1. 우선 순위 큐로 다익스트라 구현
import heapq

def dijkstar():
    dijk = [float('inf') for _ in range(N + 1)]
    dijk[0] = 0
    p_q = []
    p_q.append((0, 0))
    heapq.heapify(p_q)

    while p_q:
        _, this_node = heapq.heappop(p_q)
        for cost, next_node in go_to[this_node]:
            via = cost + dijk[this_node]
            if dijk[next_node] > via:
                dijk[next_node] = via
                heapq.heappush(p_q, (via, next_node))

    return dijk[-1]

T = int(input())
for test_case in range(1, T + 1):
    N, E = map(int, input().split())

    go_to = [[] for _ in range(N + 1)]

    for _ in range(E):
        s, e, w = map(int, input().split())
        go_to[s].append((w, e))

    print('#{} {}'.format(test_case, dijkstar()))

# 2. 아닌방법으로 구현
# def dijkstar():
#     dijk = [float('inf') for _ in range(N + 1)]
#     dijk[0] = 0
#     visit = [0 for _ in range(N + 1)]
#     visit[0] = 1
#     index = 0
    
#     while True:
#         for next_index, cost in go_to[index]:
#             if visit[next_index] == 0:
#                 via = dijk[index] + cost
#                 if via < dijk[next_index]:
#                     dijk[next_index] = via
#         visit[index] = 1

#         min_distance = float('inf')
        
#         for i in range(N + 1):
#             if min_distance > dijk[i]:
#                 if visit[i] == 1:
#                     continue
#                 index = i
#                 min_distance = dijk[i]
        
#         if min_distance == float('inf'):
#             break

#     return dijk[-1]

# T = int(input())
# for test_case in range(1, T + 1):
#     N, E = map(int, input().split())

#     go_to = [[] for _ in range(N + 1)]

#     for _ in range(E):
#         s, e, w = map(int, input().split())
#         go_to[s].append((e, w))

#     print('#{} {}'.format(test_case, dijkstar()))