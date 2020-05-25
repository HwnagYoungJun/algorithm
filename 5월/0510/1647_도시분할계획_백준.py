import sys
sys.stdin = open('1647.txt')

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = fx

N, M = map(int, input().split())
road = []

for _ in range(M):
    road.append(list(map(int, input().split())))

road.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]

min_cost = 0
for i in range(M):
    v1, v2, cost = road[i]
    if find(v1) != find(v2):
        union(v1, v2)
        min_cost += cost
        last_cost = cost

print(min_cost - last_cost)

