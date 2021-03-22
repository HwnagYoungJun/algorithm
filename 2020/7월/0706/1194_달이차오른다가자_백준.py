import collections


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    deq.append((start[0], start[1], 0, 0))
    visit = [[[0] * 64 for _ in range(M)] for _ in range(N)]
    visit[start[0]][start[1]][0] = 1

    while deq:
        row, col, keys, time = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if miro[nr][nc] == '#':
                continue
            
            if miro[nr][nc] == '1':
                return time + 1
            
            if miro[nr][nc] == 'A':
                if 1 & keys == 0:
                    continue
            elif miro[nr][nc] == 'B':
                if 2 ** 1 & keys == 0:
                    continue
            elif miro[nr][nc] == 'C':
                if 2 ** 2 & keys == 0:
                    continue
            elif miro[nr][nc] == 'D':
                if 2 ** 3 & keys == 0:
                    continue
            elif miro[nr][nc] == 'E':
                if 2 ** 4 & keys == 0:
                    continue
            elif miro[nr][nc] == 'F':
                if 2 ** 5 & keys == 0:
                    continue

            temp_keys = keys
            if type(miro[nr][nc]) == int:
                temp_keys |= miro[nr][nc]

            if visit[nr][nc][temp_keys] == 1:
                continue
            visit[nr][nc][temp_keys] = 1
            deq.append((nr, nc, temp_keys, time + 1))
            
    return -1


N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]

for row in range(N):
    for col in range(M):
        if miro[row][col] == '0':
            start = (row, col)
        if miro[row][col] == 'a':
            miro[row][col] = 1
        if miro[row][col] == 'b':
            miro[row][col] = 2 ** 1
        if miro[row][col] == 'c':
            miro[row][col] = 2 ** 2
        if miro[row][col] == 'd':
            miro[row][col] = 2 ** 3
        if miro[row][col] == 'e':
            miro[row][col] = 2 ** 4
        if miro[row][col] == 'f':
            miro[row][col] = 2 ** 5

print(bfs())