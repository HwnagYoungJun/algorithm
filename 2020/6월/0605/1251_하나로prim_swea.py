import sys
sys.stdin = open('1251.txt')
import heapq

def distance (x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    pq = []
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
                    
    dist = [float('inf') for _ in range(N)]
    visit = {i: False for i in range(N)}
    dist[0] = 0

    E = float(input())
    pq = []
    pq.append((0, 0))
    heapq.heapify(pq)

    total_cost = 0
    cnt = 0
    while pq:
        cost, this_sum = heapq.heappop(pq)
        if visit[this_sum]:
            continue
        visit[this_sum] = True
        cnt += 1
        total_cost += cost
        if cnt == N:
            break
        min_node = 0
        min_dist = float('inf')
        for i in range(N):
            if not visit[i]:
                l = distance(x_list[this_sum], y_list[this_sum], x_list[i], y_list[i])
                if l < dist[i]:
                    dist[i] = l
                    heapq.heappush(pq, (l, i))

    print("#{} {}".format(test_case, round(E * total_cost)))

        
