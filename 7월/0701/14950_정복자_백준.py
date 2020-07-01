import heapq


N, M, t = map(int, input().split())
conj = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    A, B, C = map(int, input().split())
    conj[A].append((C, B))
    conj[B].append((C, A))

pq = conj[1]
heapq.heapify(pq)

visit = {i: False for i in range(1, N + 1)}
visit[1] = True
total_cost = 0
C = 0
chk = 1
while pq:
    cost, node = heapq.heappop(pq)
    if visit[node]:
        continue
    total_cost += C + cost
    C += t
    visit[node] = True
    if chk == N:
        break
    for edge in conj[node]:
        if visit[edge[1]]:
            continue
        heapq.heappush(pq, edge)

print(total_cost)