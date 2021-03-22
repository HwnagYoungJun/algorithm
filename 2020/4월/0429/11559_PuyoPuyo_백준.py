import sys
sys.stdin = open('11559.txt')
input = sys.stdin.readline
import collections
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    global puyo
    global visit
    global bt
    deq = collections.deque()
    deq.append((r, c))
    temp = {(r, c)}
    color = puyo[r][c]
    while deq:
        row, col = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < 12 and 0 <= nc < 6:
                if (nr, nc) not in temp and puyo[nr][nc] == color:
                    visit[nr][nc] = 1
                    temp.add((nr, nc))
                    deq.append((nr, nc))
    if len(temp) >= 4:
        bt = True
        for r, c in temp:
            puyo[r][c] = '.'
    return



puyo = [list(input()) for _ in range(12)]
visit = [[0 for _ in range(6)] for _ in range(12)]
# 1. 터진다.
ppayoen = -1
while True:
    ppayoen += 1
    bt = False
    for row in range(11, -1, -1):
        for col in range(6):
            if puyo[row][col] != '.' and visit[row][col] == 0:
                bfs(row, col)

    if bt == False:
        break
    # for i in puyo:
    #     print(*i)
    # 2. 떨어진다.
    for col in range(6):
        for row1 in range(10, -1, -1):
            
            if puyo[row1][col] != '.':
                for row2 in range(row1 + 1, 12):
                    if puyo[row2][col] != '.': 
                        if row2 - 1 != row1:
                            puyo[row2 - 1][col] = puyo[row1][col]
                            puyo[row1][col] = '.'
                        # for i in puyo:
                        #     print(*i)
                        # print()
                        break
                else:
                    puyo[11][col] = puyo[row1][col]
                    puyo[row1][col] = '.'
    
    # for i in puyo:
    #     print(*i)
    # print()

print(ppayoen)
