import sys
sys.stdin = open('1753.txt')
import collections


def bfs():
    visit = [0 for _ in range(V + 1)]
    
    dijkstra = [float('inf') for _ in range (V + 1)]
    dijkstra[start] = 0
    index = start

    while True:

        for i in range(len(grape[index])):
            next_node, value = grape[index][i]
            if visit[next_node] == 0:
                via = dijkstra[index] + value
                if via < dijkstra[next_node]:
                    dijkstra[next_node] = via

        # 지금의 정점으로 부터 가장 짧은 거리에 있는 정점을 선택하는 반복문
        min_distance = float('inf')
        visit[index] = 1

        for i in range(1, V + 1):
            if visit[i] == 0 and dijkstra[i] < min_distance:
                min_distance = dijkstra[i]
                index = i

        if visit[index]:
            break

        # 최소거리가 바뀌지 않았으면 갈수가 없기때문에 탈출

    return dijkstra
        

V, E = map(int, input().split())
start = int(input())
grape = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, e = map(int, input().split())
    grape[u].append((v, e))


# 최소의 경로를 저장하는 저장소

result = bfs()
result = result[1:]

for i in result:
    if i == float('inf'):
        print("INF")
    else:
        print(i)