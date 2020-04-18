import sys
import collections
import copy
sys.stdin = open('input.txt')
def bfs(row, col, info, deep, sw, v):
    v[row][col] = 1
    deq.append((row, col, info, deep, sw, v))
    while len(deq) != 0:
        br, bc, binfo, bd, switch, bv= deq.popleft()
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < N and bv[nr][nc] == 0:
                if binfo > map_info[nr][nc]:
                    bv[nr][nc] = 1
                    cv = copy.deepcopy(bv)
                    deq.append((nr, nc, map_info[nr][nc], bd + 1, switch, cv))
                    bv[nr][nc] = 0
                elif switch == True:
                    if map_info[br][bc] > map_info[nr][nc] - K:
                        bv[nr][nc] = 1
                        cv = copy.deepcopy(bv)
                        deq.append((nr, nc, binfo - 1, bd + 1, False, cv))
                        bv[nr][nc] = 0

    return bd


T = int(input())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    map_info = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0 # 배열에서 max 뽑아내기
    deq = collections.deque()
    sv_result = float('-inf')
    for row in range(N):
        if max(map_info[row]) > max_num:
            max_num = max(map_info[row])
    
    for row in range(N):
        for col in range(N):
            if map_info[row][col] == max_num:
                visit = [[0 for _ in range(N)] for _ in range(N)]
                result = bfs(row, col, map_info[row][col], 1, True, visit)
                if result > sv_result:
                    sv_result = result
    print('#{} {}'.format(test_case, sv_result))
    
    
        


