import sys
sys.stdin = open('아기상어.txt')
import collections
import copy
def bfs(row, col, size, eat_fish, time):
    global visit
    visit[row][col] = 1
    deq.append((row, col, size, eat_fish, time))
    while len(deq) != 0:
        br, bc, bsize, beat, btime = deq.popleft()
        print(br, bc, bsize, beat, btime)
        if fish_map[br][bc] < size and fish_map[br][bc] != 0:
            deq.clear() # 덱 초기화
            visit = [[0 for _ in range(N)] for _ in range(N)]# 비지티드 초기화
            if beat == bsize:
                beat = 0
                bsize += 1
            visit[br][bc] = 1
            deq.append((br, bc, bsize, eat_fish + 1, btime + 1))
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if size >= fish_map[nr][nc] and visit[nr][nc] == 0:
                    visit[nr][nc] = 1
                    deq.append((nr, nc, bsize, beat, btime + 1))
    return btime

N = int(input())
fish_map = [list(map(int ,input().split())) for _ in range(N)]
visit = [[0 for _ in range(N)] for _ in range(N)]
deq = collections.deque()
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
for row in range(N):  # 상어의 시작위치
    for col in range(N):
        if fish_map[row][col] == 9:
            start_row = row
            start_col = col
bfs(start_row, start_col, 1, 0, 0)




