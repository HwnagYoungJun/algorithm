import sys
sys.stdin = open('17244.txt')
import collections


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def my_perm(n, k, target):
    global min_time
    if n == k:
        order_list = [start] + target + [end]
        total_time = 0
        for i in range(len(order_list) - 1):
            start_row, start_col = order_list[i]
            end_row, end_col = order_list[i + 1]
            total_time += bfs(start_row, start_col, end_row, end_col)
            if total_time > min_time:
                break
        else:
            min_time = total_time
        return
    
    for i in range(obj_cnt):
        if visit[i] == 0:
            visit[i] = 1
            my_perm(n + 1, k, target + [obj_list[i]])
            visit[i] = 0


def bfs(r, c, end_row, end_col):
    deq = collections.deque()
    deq.append((r, c, 0))
    visit = [[0 for _ in range(M)] for _ in range(N)]
    visit[r][c] = 1

    while deq:
        row, col, time = deq.popleft()
        
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if house[nr][nc] == '#':
                continue
            if visit[nr][nc] == 1:
                continue
            # 탈출 조건
            if (nr, nc) == (end_row, end_col):
                return time + 1 
            visit[nr][nc] = 1
            deq.append((nr, nc, time + 1))
    
    return '여기까지 오면 안됩니다.'


M, N = map(int, input().split())
house = [list(input()) for _ in range(N)]

obj_cnt = 0
obj_list = []
for row in range(N):
    for col in range(M):
        if house[row][col] == 'S':
            start = (row, col)
        if house[row][col] == 'X':
            obj_cnt += 1
            obj_list.append((row, col))
        if house[row][col] == 'E':
            end = (row, col)

visit = [0] * obj_cnt
min_time = float('inf')
my_perm(0, obj_cnt, [])

print(min_time)