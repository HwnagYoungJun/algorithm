import collections
import copy
import sys
sys.stdin = open('디저트 카페.txt')
def bfs(row, col, k, already, passed, swtich):
    global sv_result
    if sv_result / 2 + 1 >=  N - row:
        return
    deq.append((row, col, k, already, passed, swtich))
    while len(deq) != 0:
        br, bc, bk, b_already, b_passed, b_sw = deq.popleft()
        if br == row and bc == col:
            if b_passed[0] != 0 and b_passed[1] != 0 and b_passed[2] !=0 and b_passed[3]:
                if b_passed[0] == b_passed[2] and b_passed[1] == b_passed[3]:
                    if bk - 1 > sv_result:
                        sv_result = bk - 1

        for w in range(b_sw, b_sw + 2):
            if 0 <= w < 4:
                if w == 1 and b_passed[0] == 0:
                    continue
                if w == 2:
                    if b_passed[2] + 1 > b_passed[0]:
                        continue
                if w == 3:
                    if b_passed[3] + 1 > b_passed[1]:
                        continue               
                nr = dr[w] + br
                nc = dc[w] + bc
                if 0 <= nr < N and 0 <= nc < N:
                    if (dessert[nr][nc] not in b_already):
                        # cv = copy.deepcopy(b_visit)
                        cp = b_passed[::]
                        cp[w] += 1
                        deq.append((nr, nc, bk + 1, b_already.union({dessert[nr][nc]}), cp, w))
    if sv_result == -100:
        sv_result = -1
                    
T = int(input())
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]
for test_case in range(1, T + 1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    passed_road = [0, 0, 0, 0]
    deq = collections.deque()
    sv_result = -100
    for row in range(N - 1):
        for col in range(1, N -1):
            bfs(row, col, 1, set(), passed_road, 0)
    print('#{} {}'.format(test_case, sv_result))