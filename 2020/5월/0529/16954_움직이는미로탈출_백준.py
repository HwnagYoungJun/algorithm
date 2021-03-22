import sys
sys.stdin = open('16954.txt')
import collections

dr = [0, -1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, -1, 0, 1, 1, 1, 0, -1, 0]
def bfs():
    global wall
    deq = collections.deque()
    deq.append((7, 0, 0))
    visit = [[[0 for _ in range(8)] for _ in range(8)] for _ in range(8)]
    len_w = len(wall)
    for i in range(len_w):
        r, c = wall[i]
        if r != 7:
            wall.append((r + 1, c))
    while deq:
        # 벽이 내려옵니다.
        len_d = len(deq) 
        for _ in range(len_d):
            row, col, time = deq.popleft()
            if time == 7:
                print(1)
                return
            for w in range(9):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if (nr, nc) not in wall:
                        if visit[nr][nc][time + 1] == 0:
                            visit[nr][nc][time + 1] = 1
                            deq.append((nr, nc, time + 1))
        len_w = len(wall)
        for i in range(len_w):
            if wall[i][0] != 7:
                wall[i] = (wall[i][0] + 1, wall[i][1]) 

    print(0)

miro = [list(input()) for _ in range(8)]

wall = []
for row in range(8):
    for col in range(8):
        if miro[row][col] == '#':
            wall.append((row, col))
bfs()