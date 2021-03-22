# 1. kruscal 문제
# 2. 모든 길이 있다고 생각하고 연결하는 식으로 생각을 바꿈
# 3. 간선의 갯수는 N이 아니다. (30분 날림)
# <TIL>
# 없음

import sys
sys.stdin = open('1774.txt')

def find(x):
    if x == parrent[x]:
        return x
    parrent[x] = find(parrent[x])
    return parrent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parrent[fy] = fx

def dis(x, y):
    x1, y1 = x
    x2, y2 = y
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

N, M = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(N)]
path = []

for i in range(N - 1):
    for j in range(i + 1, N):
        cost = dis(temp[i], temp[j])
        path.append([i + 1, j + 1, cost])

parrent = [i for i in range(N + 1)]
path.sort(key=lambda x: x[2])

m_count = 0
for _ in range(M):
    god1, god2 = map(int, input().split())
    if find(god1) != find(god2):
        union(god1, god2)
        m_count += 1

min_cost = 0

for g1, g2, cost in path:
    if find(g1) != find(g2):
        union(g1, g2)
        min_cost += cost
    if m_count == N - 1:
        break

print(format(min_cost, ".2f"))