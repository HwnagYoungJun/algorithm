import sys
sys.stdin = open('test.txt')
import pprint
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def is_wall(row, col, d):
    global chk
    if 0 <= row < N and 0 <= col < N:
        return (row, col, d)

    chk += 1
    if row < 0:
        d = change_direction(d)
        return (1, col, d)
    if row >= N:
        d = change_direction(d)
        return (N - 2, col, d)
    if col < 0:
        d = change_direction(d)
        return (row, 1, d)
    if col >= N:
        d = change_direction(d)
        return (row, N - 2, d)

def change_direction(d):
    if d == 0:
        return 1
    elif d == 1:
        return 0
    elif d == 2:
        return 3
    else:
        return 2


N, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
pan = [[[] for _ in range(N)] for _ in range(N)]
chess_piece = {i: [] for i in range(1, K + 1)}


for i in range(1, K + 1):
    r, c, d = map(int, input().split())
    chess_piece[i] = [[r - 1, c - 1], d - 1]
    pan[r - 1][c - 1].append(i)

game = 0
game_over = False
while game < 1001:
    if game_over:
        break
    game += 1
    for chess_num, value in chess_piece.items():
        row, col = value[0]
        dd = value[1]
        index = pan[row][col].index(chess_num)
        move_list = pan[row][col][index:]
        chk = 0
        nr = row + dr[dd]
        nc = col + dc[dd]
        # print(nr, nc, dd)
        # for i in pan:
        #     print(*i)
        # print()
        nr, nc, dd = is_wall(nr, nc, dd)
        chess_piece[chess_num][1] = dd     
        if map_list[nr][nc] == 0:
            for i in move_list:
                pan[nr][nc].append(i)
                pan[row][col].remove(i)
                chess_piece[i][0] = [nr, nc]
        
        elif map_list[nr][nc] == 1:
            move_list = move_list[::-1]
            for i in move_list:
                pan[nr][nc].append(i)
                pan[row][col].remove(i)
                chess_piece[i][0] = [nr, nc]
        
        else:
            chk += 1
            if chk == 2:
                chess_piece[chess_num][1] = dd
            else:
                dd = change_direction(dd)
                nr = row + dr[dd]
                nc = col + dc[dd]
                nr, nc, dd = is_wall(nr, nc, dd)
                if chk == 2:
                    chess_piece[chess_num][1] = dd
                    
                else:
                    if map_list[nr][nc] == 0:
                        for i in move_list:
                            pan[nr][nc].append(i)
                            pan[row][col].remove(i)
                            chess_piece[i][0] = [nr, nc]
                            chess_piece[chess_num][1] = dd

                    elif map_list[nr][nc] == 1:
                        move_list = move_list[::-1]
                        for i in move_list:
                            pan[nr][nc].append(i)
                            pan[row][col].remove(i)
                            chess_piece[i][0] = [nr, nc]
                            chess_piece[chess_num][1] = dd

                    else:
                        chess_piece[chess_num][1] = dd

        if len(pan[nr][nc]) >= 4:
            game_over = True
            break

if game == 1001:
    print(-1)
else:
    print(game)

          
