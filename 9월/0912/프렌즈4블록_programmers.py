dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

def solution(m, n, board):
    # m : row, n: col
    answer = 0
    pan = list()
    for i in board:
        pan.append(list(i))
    
    while True:
        boom_list = set()

        # 1. 터트리기
        for row in range(m - 1):
            for col in range(n - 1):
                this_block = pan[row][col]
                if this_block == 0:
                    continue
                if pan[row][col + 1] != this_block or pan[row + 1][col] != this_block or pan[row + 1][col + 1] != this_block:
                    continue
                
                for w in range(4):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    boom_list.add((nr, nc))
        for row, col in boom_list:
            pan[row][col] = 0
        if len(boom_list) == 0:
            break

        answer += len(boom_list)
        # 2.내리기
        for col in range(n):
            for row in range(m - 2, -1, -1):
                if pan[row][col] == 0:
                    continue
                end_row = False
                for end in range(row + 1, m):
                    if end_row == True:
                        break
                    if end == m - 1 and pan[end][col] == 0:
                        pan[row][col], pan[end][col] = pan[end][col], pan[row][col]
                    if pan[end][col] != 0:
                        pan[row][col], pan[end - 1][col] = pan[end - 1][col], pan[row][col]
                        end_row = True
                        continue   
                
    return answer


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))