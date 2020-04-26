import sys
sys.stdin = open('1987.txt')
input = sys.stdin.readline
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    global cnt
    deq = collections.deque()
    deq.append((0, 0, {board[0][0]})) # r,c 와 count를 담자!
    # 방문은 루트마다 다르므로 다르게 관리한다

    while deq:
        row, col, foot_step = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] not in foot_step:
                    deq.append((nr, nc, foot_step | {board[nr][nc]}))
                    cnt = max(len(foot_step) + 1, cnt)
                    

# 첫 느낌 : SWEA의 수지의 수지맞는 여행이랑 비슷하다는 느낌을 받음

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
cnt = 1
bfs()
print(cnt)

# 끝 느낌 : dfs로 풀껄