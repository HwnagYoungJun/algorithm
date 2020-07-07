import sys
sys.stdin = open('4991.txt')
from pprint import pprint
import collections


# 10! = 약 3,600,000
# 1BFS = 20 * 20 = 400

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    deq.append((start[0], start[1], 0, 0))
    visit = [[[0] * 2 ** 10 for _ in range(M)] for _ in range(N)]
    visit[start[0]][start[1]][0] = 1

    while deq:
        row, col, time, clean = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            if room[nr][nc] == 'x':
                continue

            temp_clean = clean
            if type(room[nr][nc]) == int:
                temp_clean |= room[nr][nc]
            
            if visit[nr][nc][temp_clean] == 1:
                continue
            
            if temp_clean == dust_cnt - 1:
                return time + 1

            visit[nr][nc][temp_clean] = 1
            deq.append((nr, nc, time + 1, temp_clean))

    return -1
            

while True:

    M, N = map(int, input().split())

    if (M, N) == (0, 0):
        break

    room = [list(input()) for _ in range(N)]

    dust_list = []
    dust_num = 1

    for row in range(N):
        for col in range(M):

            if room[row][col] == 'o':
                start = (row, col)

            if room[row][col] == '*':
                room[row][col] = dust_num
                dust_num *= 2
                dust_list.append((row, col))

    dust_cnt = 2 ** len(dust_list)

    if len(dust_list) == 0:
        print(0)
    else:
        print(bfs())