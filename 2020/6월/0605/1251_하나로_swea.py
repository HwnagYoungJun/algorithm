import sys
sys.stdin = open('1251.txt')

def dist(i1, i2, g):
    return ((g[i2][0] - g[i1][0]) ** 2 + (g[i2][1] - g[i1][1]) ** 2) ** 0.5

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

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    island = []
    temp = [list(map(int, input().split())) for _ in range(2)]
    for i in range(N):
        island.append((temp[0][i], temp[1][i]))
    E_list = []
    parent = {i: i for i in range(N)}
    E = float(input())
    for i1 in range(N - 1):
        for i2 in range(i1, N):
            E_list.append((dist(i1, i2, island) ** 2, i1, i2))
    E_list.sort()
    total_cost = 0
    for cost, island1, island2 in E_list:
        if find(island1) != find(island2):
            union(island1, island2)
            total_cost += cost
    total_cost = round(total_cost * E)
    print('#{} {}'.format(test_case, total_cost))