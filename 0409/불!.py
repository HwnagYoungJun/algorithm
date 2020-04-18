import sys
sys.stdin = open('불!.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    global visit

    deq = collections.deque()
    deq.append((start_row, start_col, 0))
    visit[start_row][start_col] = 1
    sv_time = -1
    while len(deq) != 0:
        r, c, time = deq.popleft()
        if r == 0 or c == 0 or r == R - 1 or c == C - 1:
            return time + 1
        if sv_time != time:
            temp_set = fire_set.copy()
            fire_set.clear()
            for i in temp_set:
                fr, fc = i
                for w in range(4):
                    ffr = fr + dr[w]
                    ffc = fc + dc[w]
                    if 0 <= ffr < R and 0 <= ffc < C:
                        if miro[ffr][ffc] != '#' and visit[ffr][ffc] == 0:
                            fire_set.add((ffr, ffc))
                            visit[ffr][ffc] = 1
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < R and 0 <= nc < C:
                if miro[nr][nc] == '.' and visit[nr][nc] == 0:
                    if nr == 0 or nc == 0 or nr == R - 1 or nc == C - 1:
                        return time + 2
                    else:
                        visit[nr][nc] = 1
                        deq.append((nr, nc, time + 1))
        sv_time = time
    return 'IMPOSSIBLE'

R, C = map(int, input().split())

miro = [list(input()) for _ in range(R)]
chk = True
fire_set = set()
visit = [[0 for _ in range(C)] for _ in range(R)]

# 입력을 받자!
for row in range(R):
    for col in range(C):
        
        if chk == True:
            if miro[row][col] == 'J':
                start_row = row
                start_col = col
                chk = False
        
        if miro[row][col] == 'F':
            fire_row = row
            fire_col = col
            fire_set.add((fire_row, fire_col))
            visit[fire_row][fire_col] = 1
    
print(bfs())

