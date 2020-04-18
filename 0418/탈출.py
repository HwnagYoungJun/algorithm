import sys
sys.stdin = open('탈출.txt')
import collections

def bfs():
    gosum = collections.deque()
    r, c = start
    gosum.append((r, c, 0))
    gosum_visit = [[0 for _ in range(C)] for _ in range(R)]
    gosum_visit[r][c] = 1
    sv_time = -1

    while gosum:
        row, col, time = gosum.popleft()

        if sv_time != time:

            a = len(deq)
            
            for i in range(a):
                wr, wc = deq.popleft()

                for w in range(4):
                    move_row = wr + dr[w]
                    move_col = wc + dc[w]

                    if 0 <= move_row < R and 0 <= move_col < C:
                        if forest[move_row][move_col] == '.' and forest[move_row][move_col] != 'D':
                            
                            forest[move_row][move_col] = '*'
                            deq.append((move_row, move_col))

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C:
                if (forest[nr][nc] == '.' or forest[nr][nc] == 'D') and gosum_visit[nr][nc] == 0:
                    if forest[nr][nc] == 'D':
                        return time + 1
                    else:
                        gosum_visit[nr][nc] = 1
                        gosum.append((nr, nc, time + 1))

        sv_time = time
    
    return "KAKTUS"

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

R, C = map(int, input().split())

forest = [list(map(str, input())) for _ in range(R)]

deq = collections.deque()

for row in range(R):
    for col in range(C):
        if forest[row][col] == 'S':
            forest[row][col] = '.'
            start = (row, col)
        elif forest[row][col] == 'D':
            end = (row, col)
        elif forest[row][col] == '*':
            deq.append((row, col))

print(bfs())