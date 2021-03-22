import sys
sys.stdin = open('11725.txt')
import collections

def find(node):
    global result
    global visit

    deq = collections.deque()
    deq.append(node)

    while deq:
        node = deq.popleft()

        for i in V[node]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = node
                deq.append(i)

N = int(input())

V = [[] for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    V[n1].append(n2)
    V[n2].append(n1)

visit = [0 for _ in range(N + 1)]
for n in range(1, N + 1):
    if visit[n] == 0:
        visit[n] = 1
        result[n] = n
        find(n)

for i in range(2, N + 1):
    print(result[i])
