# 1. 가장 가까운 거리에 있는 치킨집 거리가 치킨거리다.
# 2. 하지만 치킨집 중에 M개만 살려야 한다.
# 3. 따라 조합으로 치킨집을 뽑아서 가장 가까운 거리를 구하는게 어떨까?
# 4. 야비하게 이터툴즈를 써서 문제를 풀어보자

import sys
sys.stdin = open('15686.txt')
from itertools import combinations

def distance(n1, n2):
    r1, c1 = n1
    r2, c2 = n2
    return abs(r2 - r1) + abs(c2 - c1)

def shortcut(n, c):
    short = float('inf')
    for i in c:
        d = distance(n, i)
        if short > d:
            short = d
    return short

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
len_h = 0
chicken = []
len_c = 0

for row in range(N):
    for col in range(N):
        if city[row][col] == 1:
            house.append((row, col))
            len_h += 1
        elif city[row][col] == 2:
            chicken.append((row, col))
            len_c +=1

result = float('inf')

for combi in combinations(chicken, M):
    total = 0
    for h in house:
        total += shortcut(h, combi)
        if result < total:
            break
    else:
        result = total

print(result)