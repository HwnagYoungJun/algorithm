import sys
sys.stdin = open('5249.txt')

# 크루스칼로 구현
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
    V, E = map(int, input().split())
    E_list = []

    for _ in range(E):
        E_list.append(list(map(int, input().split())))

    E_list.sort(key=lambda x: x[2])

    parent = [i for i in range(V + 1)]

    total_w = 0
    for n1, n2, w in E_list:
        if find(n1) != find(n2):
            union(n1, n2)
            total_w += w
    print('#{} {}'.format(test_case, total_w))