import sys
sys.stdin = open('1520.txt')
import collections

# 좌, 우, 상,
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs():
    global cnt 

    deq = collections.deque()
    deq.append((0, 0))
    
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            if possible_map[row][col][w] == False:
                continue

            nr = row + dr[w]
            nc = col + dc[w]

            # if nr < 0 or nr >= N or nc < 0 or nc >= M:
            #     continue

            if (nr, nc) == (N - 1, M - 1):
                cnt += 1
            
            deq.append((nr, nc))

        
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

possible_map = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]

for row in range(N):
    for col in range(M):

        temp = map_list[row][col]
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if map_list[nr][nc] < temp:
                    possible_map[row][col][w] = True
                    continue
        
            possible_map[row][col][w] = False

cnt = 0
bfs()
print(cnt)