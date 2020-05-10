import sys
sys.stdin = open('1197.txt')

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
    
V, E = map(int, input().split())

Elist = list()
for i in range(E):
    Elist.append(list(map(int, input().split())))

# 1. 가중치를 기준으로 정렬
Elist.sort(key=lambda x: x[2])

# 2. 유니온 파인드
parent = [i for i in range(V + 1)]

# 3. 하나씩 체크
min_cost = 0
cruscal = list()
for i in range(E):
    v1, v2, cost = Elist[i]
    # 조상이 다르다면(사이클을 이루지 않는다면)
    if find(v1) != find(v2):
        # 유니온 시켜주고 MST에 포함시켜준다.
        union(v1, v2)
        cruscal.append((v1, v2))
        min_cost += cost
print(min_cost)