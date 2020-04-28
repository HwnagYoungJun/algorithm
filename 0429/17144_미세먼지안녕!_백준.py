import sys
sys.stdin = open('17144.txt')
import collections

R, C, T = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(R)]

dust = collections.deque()
air_cleaner = list()

for r in range(R):
    for c in range(C):
        if room[r][c] == -1:
            air_cleaner.append((r, c))

        elif room[r][c] != 0:
            dust.append((r, c, room[r][c]))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
ucr, ucc = air_cleaner[0]
dcr, dcc = air_cleaner[1]
for _ in range(T):
    # 1. 먼지확산

    length = len(dust)
    for _ in range(length):

        row, col, d = dust.popleft()
        
        direction = 0
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1 and d // 5 != 0:

                direction += 1
                # if room[nr][nc] == 0:
                #     # dust.append((nr, nc, d // 5))
                # else:
                #     # dust.append((nr, nc, room[nr][nc] + d // 5))
                room[nr][nc] += d // 5
        
        # dust.append((row, col, d - (direction * (d // 5))))
        room[row][col] = room[row][col] - (direction * (d // 5))
    # print(dust)
    # for i in room:
    #     print(*i)
    # print()
    
    # ucr, ucc = air_cleaner[0]
    # dcr, dcc = air_cleaner[1]
    # 2. 공기청정기 발동
    
    for col in range(ucc, 0, -1):
        if col != ucc:
            room[ucr][col] = room[ucr][col - 1]
        room[ucr][col - 1] = 0
    for row in range(ucr - 1, -1 , -1):
        if row != ucr - 1:
            room[row + 1][0] = room[row][0]
        room[row][0] = 0

    for col in range(C - 1):
        room[0][col] = room[0][col + 1]
        room[0][col + 1] = 0
    
    for row in range(ucr):
        room[row][C - 1] = room[row + 1][C - 1]
        room[row + 1][C - 1] = 0

    for col in range(C - 1, ucc +1 , - 1):
        room[ucr][col] = room[ucr][col - 1]
        room[ucr][col - 1] = 0

    # for i in room:
    #     print(*i)
    # print()

    # 3. 아래공기 발동
    for col in range(dcc, 0, -1):
        if col != dcc:
            room[dcr][col] = room[dcr][col - 1]
        room[dcr][col - 1] = 0
    for row in range(dcr + 1, R):
        if row != dcr + 1:
            room[row - 1][0] = room[row][0]
        room[row][0] = 0

    for col in range(C - 1):
        room[R - 1][col] = room[R - 1][col + 1]
        room[R - 1][col + 1] = 0
    
    for row in range(R - 2, dcr - 1, - 1):
        room[row + 1][C - 1] = room[row][C - 1]
        room[row][C - 1] = 0

    for col in range(C - 1, dcc + 1 , - 1):
        room[dcr][col] = room[dcr][col - 1]
        room[dcr][col - 1] = 0
    # for i in room:
    #     print(*i)
    # print()
    result = 0
    for r in range(R):
        for c in range(C):
            
            if room[r][c] > 0:
                dust.append((r, c, room[r][c]))
                result += room[r][c]

print(result)
