import sys
sys.stdin = open('5247.txt')
from collections import deque

def bfs():
    limit = 1000000 + 1
    visit = [0 for _ in range(limit)]
    visit[N] = 1
    deq = deque()
    deq.append((N, 0))

    while deq:
        witch, time = deq.popleft()

        if witch == M:
            return time

        dw = [-1, 1, -10, witch]
        for w in range(4):
            nw = witch + dw[w]
            if 0 < nw < limit:
                if visit[nw] == 0:
                    visit[nw] = 1
                    deq.append((nw, time + 1))

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    result = bfs()
    print("#{} {}".format(test_case, result))