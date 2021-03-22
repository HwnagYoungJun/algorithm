import sys
sys.stdin = open('1325.txt')
import collections

def bfs(start):
    deq = collections.deque()
    deq.append(start)
    visit = [0 for _ in range(N + 1)]
    visit[start] = 1
    cnt = 0
    while deq:
        com = deq.popleft()
        for i in range(len(connetion[com])):
            w = connetion[com][i]
            if visit[w] == 0:
                visit[w] = 1
                cnt += 1
                deq.append(w)
    return cnt


N, M = map(int, input().split())
connetion = [[] for _ in range(N + 1)]

for i in range(M):
    com1, com2 = map(int, input().split())
    connetion[com2].append(com1)

result = list()
max_haking = float('-inf')
for i in range(1, N +1):
    hacking = bfs(i)
    if hacking > max_haking:
        max_haking = hacking
        result.clear()
        result.append(i)
    elif hacking == max_haking:
        result.append(i)
result.sort()
print(*result)    