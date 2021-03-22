import sys
sys.stdin = open('1781.txt')
import heapq

N = int(input())
dead_list = {i: [] for i in range(N + 1)}

max_dead = float('-inf')
for _ in range(N):
    a, b = map(int, input().split())
    max_dead = max(max_dead, a)
    dead_list[a].append(b)

pq = []
result = 0
for i in range(max_dead, 0, -1):
    for j in dead_list[i]:
        heapq.heappush(pq, -j)
    if pq:
        result -= heapq.heappop(pq)

print(result)