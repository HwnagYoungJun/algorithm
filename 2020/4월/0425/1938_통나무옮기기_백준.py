import sys
sys.stdin = open('1938.txt')
import collections

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 가로 1 세로 0
def bfs():
    visit = [[[0, 0] for _ in range(N)] for _ in range(N)] # 중앙을 기준으로하여 0 세로, 1 가로
    a, b = tree[1]
    visit[a][b] = [1,1]
    deq = collections.deque()
    deq.append((a, b, tree[3], 0))

    while deq:

        row, col, status, cnt = deq.popleft()
        # print(row, col, status, cnt)
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if status == 0: # 세로
                if 1 <= nr < N - 1 and 0 <= nc < N:
                    if ground[nr][nc] != '1' and ground[nr - 1][nc] != '1' and ground[nr + 1][nc] != '1':
                        if visit[nr][nc][0] == 0:
                            visit[nr][nc][0] = 1
                            deq.append((nr, nc, status, cnt + 1))

            else:
                if 0 <= nr < N and 1 <= nc < N - 1:
                    if ground[nr][nc] != '1' and ground[nr][nc - 1] != '1' and ground[nr][nc + 1] != '1':
                        if visit[nr][nc][1] == 0:
                            visit[nr][nc][1] = 1
                            deq.append((nr, nc, status, cnt + 1))
            
            if ([nr, nc], status) == end:
                return cnt + 1

        # 회전
        if status == 0:
            if 1 <= col < N - 1:
                if ground[row][col - 1] != '1' and ground[row][col + 1] != '1' and ground[row - 1][col + 1] != '1' and ground[row - 1][col - 1] != '1' and ground[row + 1][col - 1] != '1' and ground[row + 1][col + 1] != '1':
                    if ([row, col], 1) == end:
                        return cnt + 1
                    else:
                        if visit[row][col][1] == 0:
                            visit[row][col][1] = 1
                            deq.append((row, col, 1, cnt + 1)) 
        else:
            if 1 <= row < N - 1:
                if ground[row - 1][col] != '1' and ground[row + 1][col] != '1' and ground[row - 1][col + 1] != '1' and ground[row - 1][col - 1] != '1' and ground[row + 1][col - 1] != '1' and ground[row + 1][col + 1] != '1':
                    if ([row, col], 0) == end:
                        return cnt + 1
                    if visit[row][col][0] == 0:
                        visit[row][col][0] = 1
                        deq.append((row, col, 0, cnt + 1))
    
    return 0


N = int(input())

ground = [list(input()) for _ in range(N)]

tree = list()
end = list()
for row in range(N):
    for col in range(N):
        if ground[row][col] == 'B':
            tree.append([row, col])

        elif ground[row][col] == 'E':
            end.append([row, col])
            


if tree[0][0] == tree[1][0]:  #가로 :1 
    tree += [1]
else:
    tree += [0]

if end[0][0] == end[1][0]: # 가로 
    end = (end[1], 1)
else: # 가로로 있다면
    end = (end[1], 0) 

print(bfs())