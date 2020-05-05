import sys
sys.stdin = open('1238.txt')
import collections

def dijkstra():
    
    dijk = [float('inf') for _ in range(N + 1)]
    visit = [0 for _ in range(N + 1)]
    dijk[X] = 0
    visit[X] = 1
    index = X
    while True:

        # 다익스트라의 첫번쨰는 최신화시켜주기!
        for nc, time in connect[index]:
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

def dfs(start, i, dis):
    global temp
    visit[i] = 1
    if dis >= temp[start]:
        return
    if i == X:
        if temp[start] > dis:
            temp[start] = dis
        return
    else:

        for ni,time in connect[i]:
            if visit[ni] == 0:
                visit[ni] = 1
                dfs(start, ni, dis + time)
                visit[ni] = 0
            
N, M, X = map(int, input().split())

connect = [[] for _ in range(N + 1)]

for _ in range(M):
    S, E, T = map(int, input().split())

    connect[S].append((E, T))

귀가 = dijkstra()
temp = [float('inf') for _ in range(N + 1)]
for index in range(1, N + 1):
    if index != X:
        visit = [0 for _ in range(N + 1)]
        dfs(index, index, 0)
        귀가[index] += temp[index]
귀가[0] = float('-inf')
print(max(귀가))