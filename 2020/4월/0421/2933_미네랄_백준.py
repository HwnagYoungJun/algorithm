import sys
sys.stdin = open('2933.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
# 땅에 붙어있는가?

def claster(r, c):
    global chk
    cla = collections.deque()
    chk[r][c] = 1
    cla.append((r, c))

    while cla:
        row, col = cla.popleft()
        # print(row, col)
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C:
                if chk[nr][nc] == 0 and cave[nr][nc] == 'x':
                    chk[nr][nc] = 1
                    cla.append((nr, nc))
    
    return

# 땅에 붙어있지 않은 친구들을 떨어뜨리자
def drop():
    drop_list = collections.deque()

    for r in range(R):
        for c in range(C):
            if cave[r][c] == 'x' and chk[r][c] == 0:
                cave[r][c] = '.'
                drop_list.append((r, c))
    
    value = True
    while drop_list and value:
        for row, col in drop_list:
            if row + 1 >= R or cave[row + 1][col] == 'x':
                value = False
                break
        else:
            for idx in range(len(drop_list)):
                drop_list[idx] = (drop_list[idx][0] + 1, drop_list[idx][1])
    
    
    for rrr, ccc in drop_list:
        cave[rrr][ccc] = 'x'

    return


# 입력
R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
temp_list = list(map(int, input().split()))

for i in range(N):
    row = R - temp_list[i]
    chk = [[0 for _ in range(C)] for _ in range(R)]
    if i % 2 == 0:
        for col in range(C):
            if cave[row][col] == 'x':
                cave[row][col] = '.'
                break

    else:
        for col in range(C - 1, -1, -1):
            if cave[row][col] == 'x':
                cave[row][col] = '.'
                break

    for j in range(C):
        if cave[R - 1][j] == 'x' and chk[R - 1][j] == 0:
            claster(R - 1, j)
    # for q in chk:
    #     print(*q)
    # print()
    drop()

    for k in cave:
        print(*k)
    print()

for row in range(R):
    for col in range(C):

        if col != C - 1:
            print(cave[row][col],end='')
        else:
            print(cave[row][col])



