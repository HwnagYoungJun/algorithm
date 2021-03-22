import sys
sys.stdin = open('8972.txt')

def distance(jongsu, crazy):
    r, c = jongsu
    row, col = crazy
    min_distance = float('inf')
    npos = None
    for w in range(1, 10):
        if w == 5:
            continue
        nr = row + dr[w]
        nc = col + dc[w]

        if min_distance > abs(nr - r) + abs(nc - c):
            min_distance = abs(nr - r) + abs(nc - c)
            npos = (nr, nc)

    return npos

dr = ['No', 1, 1, 1, 0, 0, 0, -1, -1, -1]
dc = ['No', -1, 0, 1, -1, 0, 1, -1, 0, 1]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
control = list(map(int, input()))
crazy_list = []
start = ('row', 'col')

for row in range(R):
    for col in range(C):
        if board[row][col] == 'R':
            crazy_list.append((row, col))
        if board[row][col] == 'I':
            start = (row, col)

game_over = False
cnt = 0
for turn in range(1, len(control) + 1):
    row, col = start
    move = control[turn - 1]
    if move != 5:
        cnt += 1
    # 1. 종수의 아두이노를 보드에서 치우고 새로운자리에 놓는다.
    board[row][col] = '.'
    nr = row + dr[move]
    nc = col + dc[move]
    if board[nr][nc] == 'R':
        game_over = True
        break
    board[nr][nc] = 'I'
    start = (nr, nc)

    # 2. 미친 아두이노를 하나씩 움직인다.
    destroy_set = set()
    new_crazy = []
    visit = {(row, col): False for row in range(R) for col in range(C)}
    for arduino in crazy_list:
        nr, nc = distance(start, arduino)
        if board[nr][nc] == 'I':
            game_over = True
            break
        
        elif visit[(nr, nc)]:
            destroy_set.add((nr, nc))
        
        else:
            visit[(nr, nc)] = True
            new_crazy.append((nr, nc))
    
    if destroy_set:
        for destroy in destroy_set:
            new_crazy.remove(destroy)
    
    for r, c in crazy_list:
        board[r][c] = '.'
    for r, c in new_crazy:
        board[r][c] = 'R'
        
    if game_over:
        break
    
    crazy_list = new_crazy[:]

game_over = True
if game_over:
    print(f"krax {cnt}")

else:
    for row in range(R):
        for col in range(C):
            if col == C - 1:
                print(board[row][col])
            else:
                print(board[row][col], end='')