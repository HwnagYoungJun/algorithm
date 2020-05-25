import sys
sys.stdin = open('4386.txt')
input = sys.stdin.readline
from itertools import combinations

def find(x):
    if parrent[x] == x:
        return x
    parrent[x] = find(parrent[x])
    return parrent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parrent[fy] = fx
def distance(s1, s2):
    x1, y1 = s1
    x2, y2 = s2
    return round(((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5, 2)

N = int(input())

star = [0]+ [list(map(float, input().split())) for _ in range(N)]

parrent = [i for i in range(N + 1)]

Elist = list()

for combi in combinations(range(1, N + 1), 2):
    star1, star2 = combi
    Elist.append((star1, star2, distance(star[star1], star[star2])))

Elist.sort(key=lambda x: x[2])

min_cost = 0

for i in Elist:
    s1, s2, cost = i

    if find(s1) != find(s2):
        union(s1, s2)
        min_cost += cost

print(min_cost)