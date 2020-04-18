import sys
sys.stdin = open('11724.txt')
from collections import deque

def bfs(start):
    deq = deque()
    deq.append(start)
    visit[start] = 1

    while deq:
        num = deq.popleft()

        for w in range(len(grape[num])):
            if visit[grape[num][w]] == 0:
                visit[grape[num][w]] = 1
                deq.append(grape[num][w])
     
N, M = map(int, input().split())
# N : 개수, M : 간선의 개수

grape = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, input().split())
    grape[node1].append(node2)
    grape[node2].append(node1)

visit = [0 for _ in range(N + 1)]

CC = 0

for i in range(1, N + 1):
    if visit[i] == 0:
        CC += 1
        bfs(i)
print(CC)