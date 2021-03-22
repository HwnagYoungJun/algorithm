import sys
sys.stdin = open('18188.txt')
import collections

def make_d(command, dr, dc):
    if command == 'W':
        dr.append(-1)
        dc.append(0)
    elif command == 'A':
        dr.append(0)
        dc.append(-1)
    elif command == 'S':
        dr.append(1)
        dc.append(0)
    else:
        dr.append(0)
        dc.append(1)

def bfs():
    deq = collections.deque()
    deq.append((dao[0], dao[1], []))
    # visit는 필요가 없을것 같다.
    time = 0

    while deq:
        dr = []
        dc = []
        this_marid = marid[time]
        make_d(this_marid[0], dr, dc)
        make_d(this_marid[1], dr, dc)

        for _ in range(len(deq)):
            row, col, footstep = deq.popleft()
            for w in range(2):
                nr = row + dr[w]
                nc = col + dc[w]

                if 0 <= nr < H and 0 <= nc < W:
                    if map_list[nr][nc] == '@': 
                        continue
                    if w == 0:
                        foot = this_marid[0]
                    else:
                        foot = this_marid[1]
                    if (nr, nc) == dizini:
                        return (True, footstep + [foot])
                    if w == 0:
                        deq.append((nr, nc, footstep + [foot]))
                    else:
                        deq.append((nr, nc, footstep + [foot]))
            
        time += 1
        if time >= N:
            return (False, [])

    return (False, [])
    
# H 세로, W: 가로
# (i,j) -> (row, col) (1, 1)부터 시작 
# 4방향 델타
# 다오는 N번 움직임

H, W = map(int, input().split())
# . 없음, D 다오, Z 디지니, @ 블록
map_list = [list(input()) for _ in range(H)]
N = int(input())
marid = [list(input().split()) for _ in range(N)]

for row in range(H):
    for col in range(W):
        if map_list[row][col] == 'D':
            dao = (row, col)
        if map_list[row][col] == 'Z':
            dizini = (row, col)
is_posible, foot_step = bfs()

if is_posible:
    print('YES')
    for i in foot_step:
        print(i, end='')
else:
    print('NO')