import sys
sys.stdin = open('DSLR.txt')

import collections

def bfs():
    deq = collections.deque()
    deq.append((A, ''))
    visit = [0 for i in range(0, 10000)]
    visit[int(A)] = 1 
    while len(deq) != 0:
        ready, string = deq.popleft()
        for w in range(4):
            if w == 0: # D
                nw = (int(ready) * 2) % 10000
                nw = str(nw)
                foot_step = 'D'
            elif w == 1: # S
                nw = int(ready) - 1
                if nw == -1:
                    nw = 9999
                nw = str(nw)
                foot_step = 'S'
            elif w == 2: # L
                nw = ready[1:4] + ready[0]
                foot_step = 'L'
            elif w == 3: # R
                nw = ready[-1] + ready[0:3]
                foot_step = 'R'
            if int(nw) == int(B):
                return string + foot_step
            else:
                if visit[int(nw)] == 0:
                    visit[int(nw)] = 1
                    deq.append((nw, string + foot_step))


T = int(input())

for test_case in range(1, T + 1):
    A, B = input().split()

    print(bfs())