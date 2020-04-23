import sys
sys.stdin = open('17135.txt')
from itertools import combinations
import collections
import copy
N, M, D = map(int, input().split())

game = [list(map(int, input().split())) for _ in range(N)]
temp_enermys = collections.deque()
for r in range(N):
    for c in range(M):
        if game[r][c] == 1:
            temp_enermys.append((r, c))


max_cnt = float('-inf')
for case in combinations(range(0, M), 3):
    enermys = copy.deepcopy(temp_enermys)
    cnt = 0
    while enermys:
        temp = set()
        for archer in case:
            ar, ac = N, archer
            min_len = float('inf')
            temp_shoot = '없음'
            for enermy in range(len(enermys)):
                er, ec = enermys[enermy]
                dis = abs(er - ar) + abs(ec - ac)
                if dis <= D:
                    if  dis < min_len:
                        min_len = dis
                        temp_shoot = (er, ec)
                        sc = ec
                    elif dis == min_len:
                        if ec < sc:
                            temp_shoot = (er, ec)
                            sc = ec
                    
            if temp_shoot != "없음":
                temp.add(temp_shoot)
        
        for shoot in temp:
            enermys.remove(shoot)
            cnt += 1

        length = len(enermys)
        for go in range(length):
            r, c = enermys.popleft()
            if r + 1 < N:
                enermys.append((r + 1, c))
        
    if cnt > max_cnt:
        max_cnt = cnt
print(max_cnt)
            
                


