import sys
sys.stdin = open('7569.txt')
import collections

def bfs():
    global amount_of_tomato

    while deq:
        height, row, col, time = deq.popleft()

        for w in range(6):
            nh = height + dh[w]
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if tomato[nh][nr][nc] == 0:
                    tomato[nh][nr][nc] = 1
                    amount_of_tomato -= 1
                    if amount_of_tomato == 0:
                        return time + 1
                    else:
                        deq.append((nh, nr, nc, time + 1))

    return -1
            

deq = collections.deque()

M, N, H = map(int, input().split())
# M : col, N : row

dc = [0, 0, -1, 1, 0, 0]
dr = [-1, 1, 0, 0, 0, 0]
dh = [0, 0, 0, 0 , -1, 1]
tomato = list()

for i in range(H):
    box = [list(map(int, input().split())) for _ in range(N)]
    tomato.append(box)

amount_of_tomato = 0

for height in range(H):
    for row in range(N):
        for col in range(M):
            if tomato[height][row][col] == 1:
                deq.append((height, row, col, 0))
            elif tomato[height][row][col] == 0:
                amount_of_tomato += 1
if amount_of_tomato == 0:
    print(0)
else:
    print(bfs())