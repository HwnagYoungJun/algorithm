import sys
sys.stdin = open('탈주범 검거.txt')
import collections
def case(gujomul):
    if gujomul == 1:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
    elif gujomul == 2:
        dx = [-1, 1]
        dy = [0, 0]
    elif gujomul == 3:
        dx = [0, 0]
        dy = [-1, 1]
    elif gujomul == 4:
        dx = [0, -1]
        dy = [1, 0]
    elif gujomul == 5:
        dx = [0, 1]
        dy = [1, 0]
    elif gujomul == 6:
        dx = [0, 1]
        dy = [-1, 0]
    elif gujomul == 7:
        dx = [0, -1]
        dy = [-1, 0]
    possible = list()
    for i in range(len(dx)):
            possible.append([dx[i], dy[i]])
    return (dx, dy, possible)

def bfs(row, col, k): # k = 깊이
    global count
    visit[row][col] = 1
    deq.append((row, col, k))
    while len(deq) != 0:
        br, bc, bk = deq.popleft()
        if bk == L: 
            continue
        pipe = ziha_map[br][bc]
        dr, dc, xp = case(pipe) # xp는 안씀
        if pipe == 1:
            loop = 4
        else:
            loop = 2
        for w in range(loop):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                next_pipe = ziha_map[nr][nc] # 다음 파이프가
                if ziha_map[nr][nc] != 0:
                    xr, xc, possi = case(next_pipe) # 이전 파이프랑 연결되어 있다면 # xr, xc 는 안씀
                    for i in possi:
                        if [-dr[w], -dc[w]] == i:
                            if visit[nr][nc] == 0:
                                visit[nr][nc] = 1
                                count += 1
                                deq.append((nr, nc, bk + 1))
    return

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split()) # R : start_row C : start_col
    ziha_map = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0 for _ in range(M)] for _ in range(N)]
    deq = collections.deque()
    count = 1
    bfs(R, C, 1)
    print('#{} {}'.format(test_case, count))