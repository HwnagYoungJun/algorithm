import sys
sys.stdin = open('2887.txt')
import heapq

# def dis(n1, n2, arr):
#     x1, y1, z1 = arr[n1]
#     x2, y2, z2 = arr[n2]
#     return min(abs(x2 - x1), abs(y2 - y1), abs(z2 - z1))

# N = int(input())
# planet = [list(map(int, input().split())) for _ in range(N)]

# pq = []
# heapq.heappush(pq, (0, 0)) # (a, b), a = 거리, b = 지금의위치
# visit = {i: False for i in range(N)}
# min_dist = 0
# while pq:
#     cost, node = heapq.heappop(pq)
#     if visit[node] == False:
#         visit[node] = True
#         min_dist += cost
#         for next_node in range(N):
#             if visit[next_node] == False and node != next_node:
#                 heapq.heappush(pq, (dis(node, next_node, planet), next_node))



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

N = int(input())

x_list = []
y_list = []
z_list = []

for i in range(N):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

E_list = []
for i in range(N - 1):
    E_list.append((x_list[i + 1][0] - x_list[i][0], x_list[i][1], x_list[i + 1][1]))
    E_list.append((y_list[i + 1][0] - y_list[i][0], y_list[i][1], y_list[i + 1][1]))
    E_list.append((z_list[i + 1][0] - z_list[i][0], z_list[i][1], z_list[i + 1][1]))

parent = {i: i for i in range(N)}
E_list.sort()

min_dist = 0
for cost, planet1, planet2 in E_list:
    if find(planet1) != find(planet2):
        union(planet1, planet2)
        min_dist += cost

print(min_dist)
