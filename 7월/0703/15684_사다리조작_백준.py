import sys
sys.stdin = open('15684.txt')


def my_com(n, k, ladder, r, c):
    global possible
    if possible == True:
        return

    if n == k:
        for col in range(1, M):
            if not bfs(col, ladder):
                break
        else:
            possible = True
            return

        return

    for row in range(r, N + 1):
        for col in range(1, M):
            if row == r and col <= c:
                continue
            if ladder[row][col] == 1:
                continue
            if col > 1:
                if ladder[row][col - 1] == 1:
                    continue
            if col < M:
                if ladder[row][col + 1] == 1:
                    continue
            
            ladder[row][col] = 1
            my_com(n + 1, k, ladder, row, col)
            ladder[row][col] = 0


def bfs(start, ladder):
    row = 1
    col = start
    mode = 0 # 0:위에서 내려옴, 1: 옆으로 타고옴
    while True:
        if mode == 0:
            if ladder[row][col] == 1:
                col += 1
                mode = 1
            elif ladder[row][col - 1] == 1:
                col -= 1
                mode = 1
            else:
                row += 1
        else:
            mode = 0
            row += 1

        if row == N + 1:
            if col == start:
                return True
            else:
                return False


M, H, N = map(int, input().split())

ladder = [[0 for _ in range(M + 1)] for _ in range(N + 1)]

for _ in range(H):
    a, b = map(int, input().split())
    ladder[a][b] = 1

possible = False
for num in range(0, 4):
    my_com(0, num, ladder, 1, 0)
    if possible == True:
        print(num)
        break
else:
    print(-1)