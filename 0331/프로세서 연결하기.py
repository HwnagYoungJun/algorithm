import sys
sys.stdin = open("프로세서 연결하기.txt")

def dfs(i, length, core):
    global min_length
    global max_core

    global count
    count += 1
    if i == len(core_list):
        if max_core < core:
            max_core = core
            min_length = length
        elif max_core == core:
            if min_length > length:
                # for i in mexynos:
                #     print(*i)
                # print(min_length, length)
                min_length = length 
        return
    r, c = core_list[i]


    for w in range(5):
        if w == 0:
            dfs(i + 1, length, core)
        elif w == 1:
            swi = True
            for x in range(0, r):
                if mexynos[x][c] == 1:
                    for y in range(0, x):
                        mexynos[y][c] = 0
                    swi = False
                    break
                else:
                    mexynos[x][c] = 1
            if swi == True:
                dfs(i + 1, length + r, core + 1)
                for z in range(0, r):
                    mexynos[z][c] = 0

        elif w == 2:
            swi = True
            for x in range(r + 1, N):
                if mexynos[x][c] == 1:
                    for y in range(r + 1, x):
                        mexynos[y][c] = 0
                    swi = False
                    break
                else:
                    mexynos[x][c] = 1
            if swi == True:
                dfs(i + 1, length + (N - r - 1), core + 1)
                for z in range(r + 1, N):
                    mexynos[z][c] = 0

        elif w == 3:
            swi = True
            for x in range(0, c):
                if mexynos[r][x] == 1:
                    for y in range(0, x):
                        mexynos[r][y] = 0
                    swi = False
                    break
                else:
                    mexynos[r][x] = 1
            if swi == True:
                dfs(i + 1, length + c, core + 1)
                for z in range(0, c):
                    mexynos[r][z] = 0

        elif w == 4:
            swi = True
            for x in range(c + 1, N):
                if mexynos[r][x] == 1:
                    for y in range(c + 1, x):
                        mexynos[r][y] = 0
                    swi = False
                    break
                else:
                    mexynos[r][x] = 1
            if swi == True:
                dfs(i + 1, length + (N - c - 1), core + 1)
                for z in range(c + 1, N):
                    mexynos[r][z] = 0
            
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    mexynos = [list(map(int, input().split())) for _ in range(N)]
    core_list = list()
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if mexynos[row][col] == 1:
                core_list.append((row, col))
    max_core = float('-inf')
    min_length = float('inf')
    count = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(test_case, min_length))


