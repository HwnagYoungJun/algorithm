import sys
sys.stdin = open('미로의 거리.txt')
import collections


def start():
    for row in range(N):
        for col in range(N):
            if miro[row][col] == '2':
                return (row, col)

def bfs(row, col, k):
    visit = [[0 for _ in range(N)] for _ in range(N)]
    deq.append((row, col, k))
    visit[row][col] = 1

    while len(deq) != 0:
        br, bc, bk = deq.popleft()
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if visit[nr][nc] == 0 :
                    if miro[nr][nc] == '0':
                        visit[nr][nc] = 1
                        deq.append((nr, nc, bk + 1))
                    elif miro[nr][nc] == '3':
                        return bk
    return 0

T = int(input())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for test_case in range(1, T + 1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]
    deq = collections.deque()
    start_row, start_col = start()
    result = bfs(start_row, start_col, 0)

    print("#{} {}".format(test_case, result))