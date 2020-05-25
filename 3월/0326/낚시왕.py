import sys
sys.stdin = open("낚시왕.txt")
import collections

R, C, M = map(int, input().split())

deq = collections.deque()
for _ in range(M):
    r, c, s, d, z = map(int,input().split())  # s:속력, d:이동방향(상하우좌), z:크기
    deq.append((r, c, s, d, z))
result = 0
for king_fishing in range(1, C + 1):
    min_row = float('inf')
    fishing = 0
    for i in range(len(deq)):
        if deq[i][1] == king_fishing:
            if min_row > deq[i][0]:
                min_row = deq[i][0]
                fishing = deq[i]
    if fishing != 0:
        result += fishing[4]
        deq.remove(fishing)
        
    shark_map = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    cnt = len(deq)
    if len(deq) != 0:
        for _ in  range(cnt):
            br, bc, bs, bd, bz = deq.popleft()
            nr = br
            nc = bc
            cnt = 0
            if bd == 1:
                if bs >= 2 * (R - 1):
                    bs = bs % (2 * (R -1))
                nr = nr - bs
                if nr < 1:
                    nr = 1 + (1 - nr)
                    bd = 2
                    if nr > R:
                        nr = 2 * R - (nr)
                        bd = 1
            elif bd == 2: 
                if bs >= 2 * (R - 1):
                    bs = bs % (2 * (R - 1))
                nr = nr + bs
                if nr > R:
                    nr = 2 * R - (nr)
                    bd = 1
                    if nr < 1:
                        nr = 1 + (1 - nr)
                        bd = 2
            elif bd == 3: 
                if bs >= 2 * (C - 1):
                    bs = bs % (2 * (C - 1))
                nc = nc + bs
                if nc > C:
                    nc = 2 * C - (nc)
                    bd = 4
                    if nc < 1:
                        nc = 1 + (1 - nc)
                        bd = 3
            elif bd == 4: 
                if bs >= 2 * (C - 1):
                    bs = bs % (2 * (C -1))
                nc = nc - bs
                if nc < 1:
                    nc = 1 + (1 - nc)
                    bd = 3
                    if nc > C:
                        nc = 2 * C - (nc)
                        bd = 4
            if shark_map[nr][nc] == 0:
                shark_map[nr][nc] = (bs, bd, bz)
                deq.append((nr, nc, bs, bd, bz))
                cnt -= 1
            else:
                if shark_map[nr][nc][2] < bz:
                    ts, tb, tz = shark_map[nr][nc]
                    shark_map[nr][nc] = (bs, bd, bz)
                    deq.remove((nr, nc, ts, tb, tz))
                    deq.append((nr, nc, bs, bd, bz))
                    cnt -= 1

print(result)