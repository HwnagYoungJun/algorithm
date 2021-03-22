import sys
sys.stdin = open('2637.txt')
import collections


N = int(input())
M = int(input())

adj = {i: [] for i in range(1, N + 1)}
require_part = {i: dict() for i in range(1, N + 1)}
indegree = {i: 0 for i in range(1, N + 1)}
a = {i: 0 for i in range(1, N + 1)}

for _ in range(M):
    X, Y, K = map(int, input().split())
    adj[Y].append((X, K))
    indegree[X] += 1
print(adj)
deq = collections.deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        deq.append(i)

while deq:
    part = deq.popleft()

    for next_part, part_num in adj[part]:

        if require_part.get(next_part) != None:
            require_part[next_part][part] = part_num
        else:
            require_part[next_part][part] += part_num
        
        indegree[next_part] -= 1

        if indegree[next_part] == 0:
            deq.append(next_part)

print(require_part)