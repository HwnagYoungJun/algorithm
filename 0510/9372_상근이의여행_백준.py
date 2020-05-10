import sys
sys.stdin = open('9372.txt')

# 굳이 MST로 풀어보자

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

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    plane = []
    for _ in range(M):
        plane.append(list(map(int, input().split())))

    parent = [i for i in range(N + 1)]

    min_cost = 0

    for i in range(M):
        c1, c2 = plane[i]
        if find(c1) != find(c2):
            union(c1, c2)
            min_cost += 1

    print(min_cost)