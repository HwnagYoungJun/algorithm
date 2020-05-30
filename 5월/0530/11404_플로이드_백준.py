# 1. 플로이드 와샬 기초
# <TIL>
# 1. 플로이드 와샬
# 2. O(n^3)
# 3. 바로가는거보다 경유해서 가는것이 더 빠르다면 변경 

import sys
sys.stdin = open('11404.txt')
input = sys.stdin.readline

n = int(input())
m = int(input())

# 1. 연결행렬을 만든다.
INF = float('inf')
bus_list = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bus_list[a - 1][b - 1] = min(bus_list[a - 1][b - 1], c)

# 2. 플로이드 워셜 알고리즘

for mid in range(n): # 중간 경로 for문이 제일 상위로 와야 누락 되지 않는다.
    for start in range(n):
        for end in range(n):
            if start == end: # 자기 자신으로 오는 경우는 없으므로 0
                bus_list[start][end] = 0
            else:
                bus_list[start][end] = min(bus_list[start][end], bus_list[start][mid] + bus_list[mid][end])

for row in range(n):
    for col in range(n):
        if bus_list[row][col] == INF:
            bus_list[row][col] = 0

for i in bus_list:
    print(*i)   
