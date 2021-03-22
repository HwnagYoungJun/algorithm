import sys
sys.stdin = open("배열 돌리기4.txt")
from itertools import permutations
import collections

N, M, K = map(int, input().split())
array = [list(map(int, input().split())) for i in range(N)]

rotate = [list(map(int, input().split())) for _ in range(K)]
a = [i for i in range(1, K + 1)]
deq = collections.deque()
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
print(rotate)
perm = permutations(a, K)
for i in list(perm):
    for j in i:
        rcs = rotate[j - 1]
        count = 0
        
        r = rcs[0]
        c = rcs[1]
        s = rcs[2]
        print(r, c , s)
        row = r - s - 1
        col = c - s - 1
        s_r = r - s - 1
        s_c = c - s - 1
        e_r = r + s - 1
        e_c = c + s - 1
        w = 0
        while True:
            print(row, col)
            count += 1
            if count == N * M:
                break
            nr = row + dr[w]
            nc = col + dc[w]
            print(nr, nc)
            if nc == e_c + 1:
                print("case1")
                nc -= 1
                w = 1
                nr += 1
                e_c -= 1
            elif nr == e_r + 1:
                print("case2")
                nr -= 1
                w = 2
                nc -= 1
                e_r -= 1
            elif nc == s_c - 1:
                print("case3")
                nc += 1
                nr -= 1
                w = 3
                s_c += 1
            elif nr == s_r:
                print("case4")
                nr += 1
                nc += 1
                w = 0
                s_r += 1
            deq.append((nr, nc))
            row = nr
            col = nc
        print(deq)
