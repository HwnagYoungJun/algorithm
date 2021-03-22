import sys
sys.stdin = open('13904.txt')
import heapq

N = int(input())
dead_line = dict()
max_time = float('-inf')
for _ in range(N):
    d, w = map(int, input().split())
    max_time = max(max_time, d)
    if dead_line.get(d) == None:
        dead_line[d] = [w]
    else: 
        dead_line[d].append(w)
pq = []
max_score = 0
for i in range(max_time, 0, -1):
    if dead_line.get(i) != None:
        for j in dead_line[i]:
            heapq.heappush(pq, -j)
    if pq:
        max_score += heapq.heappop(pq)

print(-max_score)

 
