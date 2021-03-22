import sys
sys.stdin = open('1238.txt')
import collections

def dijkstra(g):
    
    dijk = [float('inf') for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]
    dijk[X] = 0
    visit[X] = 1
    index = X
    while True:

        # 다익스트라의 첫번쨰는 최신화시켜주기!
        for nc, time in g[index]:
            if visit[nc] == 0:
                via = dijk[index] + time
                if dijk[nc] > via:
                    dijk[nc] = via
        
        visit[index] = 1
        min_distance = float('inf')

        for ni in range(1, N + 1):
            if visit[ni] == 0 and min_distance > dijk[ni]:
                min_distance = dijk[ni]
                index = ni

        if min_distance == float('inf'):
            break

    return dijk

N, M, X = map(int, input().split())

connect = [[] for _ in range(N + 1)]
rev_connect = [[] for _ in range(N + 1)]
for _ in range(M):
    S, E, T = map(int, input().split())
    connect[S].append((E, T))
    rev_connect[E].append((S, T))

귀가 = dijkstra(connect)
역귀가 = dijkstra(rev_connect)
result = float('-inf')

for i in range(1, N + 1):
    if result < 귀가[i] + 역귀가[i]:
        result = 귀가[i] + 역귀가[i]

print(result)