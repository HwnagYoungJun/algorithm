import sys
sys.stdin = open('13460.txt')
import collections


def find():
    red = False
    blue = False
    hole = False
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if board[row][col] == 'R':
                red = (row, col)
                if blue != False and hole != False:
                    return red, blue, hole

            if board[row][col] == 'B':
                blue = (row, col)
                if red != False and hole != False:
                    return red, blue, hole
                    
            if board[row][col] == 'O':
                hole = (row, col)
                if red != False and blue != False:
                    return red, blue, hole

    return '뭔가 잘못되었음'
                    
def bfs():
    rr, rc = Red
    br, bc = Blue
    deq = collections.deque()
    deq.append((rr, rc, br, bc, 0))
    visit = [[[] for _ in range(M)] for _ in range(N)]
    visit[rr][rc].append((br, bc))

    while deq:
        redr, redc, bluer, bluec, cnt = deq.popleft()
        print(redr, redc, bluer, bluec, cnt)
        if cnt == 10:
            return -1
        for w in range(4):
            print(w)
            if w == 0: 
                if redr == bluer:
                    if redc < bluec:
                        for i in range(redc, -1, -1):
                            if board[redr][i] == '#':
                                redc = i + 1
                                break
                            elif board[redr][i] == 'O':
                                return cnt + 1
                        for j in range(bluec, -1, -1):
                            print(redc, j, board[bluer][j])
                            if board[bluer][j] == '#' or redc == j:
                                bluec = j + 1
                                break
                            elif board[bluer][j] == 'O':
                                break
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))                      

                    if redc > bluec:
                        for j in range(bluec, -1, -1):
                            if board[bluer][j] == '#':
                                bluec = j + 1
                                break
                            elif board[bluer][j] == 'O':
                                break
                        for i in range(redc, -1, -1):
                            if board[redr][i] == '#' or bluec == i:
                                redc = i + 1
                                break
                            elif board[redr][i] == 'O':
                                return cnt + 1
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))             

                else:
                    for i in range(redc, -1, -1):
                        if board[redr][i] == '#':
                            redc = i + 1
                            break
                        elif board[redr][i] == 'O':
                            return cnt + 1

                    for i in range(bluec, -1, -1):
                        if board[bluer][i] == '#':
                            bluec = i + 1
                            break
                        elif board[bluer][i] == 'O':
                            break 
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))              
            elif w == 1:
                if redr == bluer:
                    if redc > bluec:
                        for i in range(redc, N):
                            if board[redr][i] == '#':
                                redc = i - 1
                                break
                            elif board[redr][i] == 'O':
                                return cnt + 1
                        for j in range(bluec, N):
                            if board[bluer][j] == '#' or redc == j:
                                bluec = j - 1
                                break
                            elif board[bluer][j] == 'O':
                                break
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))            
                    if redc < bluec:
                        for j in range(bluec, N):
                            if board[bluer][j] == '#':
                                bluec = j - 1
                                break
                            elif board[bluer][j] == 'O':
                                break
                        for i in range(redc, N):
                            if board[redr][i] == '#' or bluec == i:
                                redc = i - 1
                                break
                            elif board[redr][i] == 'O':
                                return cnt + 1
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))  

                else:
                    for i in range(redc, N):
                        if board[redr][i] == '#':
                            redc = i + 1
                            break
                        elif board[redr][i] == 'O':
                            return cnt + 1

                    for i in range(bluec, N):
                        if board[bluer][i] == '#':
                            bluec = i + 1
                            break
                        elif board[redr][i] == 'O':
                            continue
                    if (bluer, bluec) not in visit[redr][redc]:
                        visit[redr][redc].append((bluer, bluec))
                        deq.append((redr, redc, bluer, bluec, cnt + 1))  
            elif w == 2:  # 상
                if redc == bluec:
                    if redr < bluer:
                        for i in range(redr, -1, -1):
                            if board[i][redc] == '#':
                                redr = i + 1
                                break
                            elif board[i][redc] == 'O':
                                return cnt + 1
                        for j in range(bluer, -1, -1):
                            if board[j][bluec] == '#' or redr == j:
                                bluer = j + 1
                                break

                            elif board[j][bluec] == 'O':
                                break

                    if redc > bluec:
                        for j in range(bluer, -1, -1):
                            if board[j][bluec] == '#':
                                bluer = j + 1
                                break
                            elif board[j][bluec] == 'O':
                                break
                        for i in range(redr, -1, -1):
                            if board[i][redc] == '#' or bluer == i:
                                redr = i + 1
                                break
                            elif board[i][redc] == 'O':
                                return cnt + 1
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))  

                else:
                    for i in range(redr, -1, -1):
                        if board[i][redc] == '#':
                            redc = i + 1
                            break
                        elif board[i][redc] == 'O':
                            return cnt + 1

                    for i in range(bluer, -1, -1):
                        if board[i][bluec] == '#':
                            bluer = i + 1
                            break
                        elif board[i][bluec] == 'O':
                            break
                    if (bluer, bluec) not in visit[redr][redc]:
                        visit[redr][redc].append((bluer, bluec))
                        deq.append((redr, redc, bluer, bluec, cnt + 1))  
            elif w == 3:  # 하
                if redc == bluec:
                    if redr > bluer:
                        for i in range(redr, N):
                            if board[i][redc] == '#':
                                redr = i -1
                                break
                            elif board[i][redc] == 'O':
                                return cnt + 1
                        for j in range(bluer, N):
                            if board[j][bluec] == '#' or redr == j:
                                bluer = j - 1
                                break

                            elif board[j][bluec] == 'O':
                                break
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))  

                    if redc > bluec:
                        for j in range(bluer, N):
                            if board[j][bluec] == '#':
                                bluer = j - 1
                                break
                            elif board[j][bluec] == 'O':
                                break
                        for i in range(redr, N):
                            if board[i][redc] == '#' or bluer == i:
                                redr = i - 1
                                break
                            elif board[i][redc] == 'O':
                                return cnt + 1
                        if (bluer, bluec) not in visit[redr][redc]:
                            visit[redr][redc].append((bluer, bluec))
                            deq.append((redr, redc, bluer, bluec, cnt + 1))  

                else:
                    for i in range(redr, N):
                        if board[i][redc] == '#':
                            redc = i - 1
                            break
                        elif board[i][redc] == 'O':
                            return cnt + 1

                    for i in range(bluer, N):
                        if board[i][bluec] == '#':
                            bluer = i - 1
                            break
                        elif board[i][bluec] == 'O':
                            break
                    if (bluer, bluec) not in visit[redr][redc]:
                        visit[redr][redc].append((bluer, bluec))
                        deq.append((redr, redc, bluer, bluec, cnt + 1))            


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]

Red, Blue, Hole = find()

print(bfs())



            