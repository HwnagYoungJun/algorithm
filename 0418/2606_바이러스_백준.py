import sys
sys.stdin = open('2606.txt')
from collections import deque

def bfs(start, infest_com):
    deq = deque()
    deq.append(start)
    
    visit = [False for _ in range(N + 1)]
    visit[start] = True

    while deq:
        infest = deq.popleft()


        for i in range(len(link_computer[infest])):

            if visit[link_computer[infest][i]] == False:
                visit[link_computer[infest][i]] = True
                infest_com += 1
                deq.append(link_computer[infest][i])
    
    return infest_com


N = int(input())
case = int(input())

link_computer = [[] for _ in range(N + 1)]
for i in range(case):
    com1, com2 = map(int, input().split())
    link_computer[com1].append(com2)
    link_computer[com2].append(com1)

print(bfs(1, 0))