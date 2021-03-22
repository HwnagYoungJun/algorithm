import sys
sys.stdin = open('1922.txt')

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

# 크루스칼(MST) 기초문제
N = int(input())
M = int(input())

connect = list()
for _ in range(M):
    connect.append(list(map(int, input().split())))

# 1. 가중치로 리스트를 정리한다.
connect.sort(key=lambda x: x[2])

# 2. 유니온 파인드를 준비한다. (find, union)
parent = [i for i in range(N + 1)]

# 3. 정령된 간선을 하나씩 검사한다.
total_cost = 0
# cruscal = list()
for i in range(M):
    v1, v2, cost = connect[i]
    # 부모가 다르다면 즉, 사이클을 이루지 않는다면
    if find(v1) != find(v2):
        # 유니온 시켜줍니다.
        union(v1, v2)
        # cruscal.append((v1, v2)) # 만약 간선을 체크해야된다면 위의 리스트에 따로 저장합니다.
        total_cost += cost

print(total_cost)