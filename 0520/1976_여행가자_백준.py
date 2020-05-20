import sys
sys.stdin = open('1976.txt')

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


N = int(input())
M = int(input())

info = [list(map(int, input().split())) for _ in range(N)]

city = []
for row in range(N):
    for col in range(N):
        if info[row][col] == 1:
            city.append((row + 1, col + 1))

parrent = [i for i in range(N + 1)]

for r, c in city:
    if find(r) != find(c):
        union(r, c)

travel = list(map(int, input().split()))
root = travel[0]
for go in travel:
    if find(root) != find(go):
        print('NO')
        break
else:
    print('YES')