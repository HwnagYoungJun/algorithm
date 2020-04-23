import sys
sys.stdin = open('17471.txt')
from itertools import combinations
import collections

def bfs(gu):
    for i in gu:
        deq = collections.deque()
        deq.append(i)
        visit = [1 for _ in range(N + 1)]
        for cango in gu:
            visit[cango] = 0
        visit[i] = 1
        while deq:
            witch = deq.popleft()
            for w in range(len(injub[witch])):
                nex = injub[witch][w]

                if visit[nex] == 0:
                    visit[nex] = 1
                    deq.append(nex)

        for c in gu:
            if visit[c] == 0:
                return False
    saram = 0
    
    for people in gu:
        saram += ingu[people]    

    return saram

N = int(input())

ingu = list(map(int, input().split()))
ingu = [0] + ingu

injub = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    Q = temp[0]
    for j in range(Q):
        injub[i].append(temp[j + 1])

# print(injub)
min_cha_e = float('inf')
for i in range(1, int(N / 2) + 1):
    for case in combinations(range(1, N + 1), i):
        A = list(case)
        B = list(range(1, N + 1))
        for b in A:
            B.remove(b)
        possi_A = bfs(A)
        if possi_A != False:
            possi_B = bfs(B)
            if possi_B != False:

                if min_cha_e > abs(possi_A - possi_B):
                    min_cha_e = abs(possi_A - possi_B)

if min_cha_e == float('inf'):
    min_cha_e = -1
print(min_cha_e)

            
