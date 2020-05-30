import sys
sys.stdin = open('1956.txt')
input = sys.stdin.readline

V, E = map(int, input().split())

# 1. 연결행렬 제작
map_list = [[float('inf') for _ in range(V)] for _ in range(V)]

for _ in range(E):
    a, b, c = map(int, input().split())
    map_list[a - 1][b - 1] = min(map_list[a - 1][b - 1], c)

for mid in range(V):
    for start in range(V):
        for end in range(V):
            if start == end:
                map_list[start][start] = 0
            else:
                map_list[start][end] = min(map_list[start][end], map_list[start][mid] + map_list[mid][end])

min_cycle = float('inf')

for row in range(V - 1):
    for col in range(row + 1, V):
        min_cycle = min(min_cycle, map_list[row][col] + map_list[col][row])

if min_cycle == float('inf'):
    min_cycle = -1

print(min_cycle)