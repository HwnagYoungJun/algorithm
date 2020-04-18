import sys
sys.stdin = open("최소 환승 경로.txt")

from collections import deque

def bfs():
    queue = deque()
    cnt = 0
    for i in end_idx:
        visited_subway[i] = 1
        for j in graph[i]:
            if j == start:
                return 0
            if visited[j] == 0:
                queue.append(j)
                visited[j] = 1
    while queue:
        for _ in range(len(queue)):
            now = queue.popleft()
            for subway in data[now]:
                if visited_subway[subway] == 0:
                    visited_subway[subway] = 1
                    for i in graph[subway]:
                        if i == start:
                            return cnt+1
                        if visited[i] == 0:
                            queue.append(i)
                            visited[i] = 1
        cnt += 1
    return -1

N, L = map(int, input().split())
graph = []
data = [[] for _ in range(N+1)]
for j in range(L):
    temp = set(map(int, input().split()))
    temp.remove(-1)
    for i in temp:
        data[i].append(j)
    graph.append(temp)
start, end = map(int, input().split())
visited = [0] * (N+1)
visited_subway = [0] * L
end_idx = []
for i in range(len(graph)):
    if end in graph[i]:
        end_idx.append(i)
print(end_idx)
print(bfs())