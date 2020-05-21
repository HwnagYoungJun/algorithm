import sys
sys.stdin = open('1185.txt')
import collections

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = parent[fx]


N, P = map(int, input().split())

parent = [i for i in range(N + 1)]

temp = [0]
start_value = float('inf')
for i in range(N):
    cost = int(input())
    temp.append(cost)
    if start_value > cost:
        start_value = cost

road = []

for _ in range(P):
    S, E, L = map(int, input().split())
    road.append((S, E, 2 * L + temp[S]+ temp[E]))

road.sort(key=lambda x: x[2])
total = 0

for n1, n2, cost in road:

    if find(n1) != find(n2):
        union(n1, n2)
        total += cost
    
print(total + start_value)