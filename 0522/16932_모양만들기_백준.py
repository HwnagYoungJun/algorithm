import sys
sys.stdin = open('16932.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    deq = collections.deque()
    deq.append((r, c))
    count = 1
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if array[nr][nc] == 1:
                    array[nr][nc] = cnt
                    deq.append((nr, nc))
                    count += 1
    return count

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
temp = ['쓰지', '않는곳']
cnt = 1
for row in range(N):
    for col in range(M):
        if array[row][col] == 1:
            cnt += 1
            array[row][col] = cnt
            temp.append(bfs(row, col))

temp_list = [[set() for _ in range(M)] for _ in range(N)]
result = float('-inf')
for row in range(N):
    for col in range(M):
        if array[row][col] == 0:
            pos_hap = 1
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]    
                if 0 <= nr < N and 0 <= nc < M:
                    if array[nr][nc] != 0:
                        if array[nr][nc] not in temp_list[row][col]:
                            temp_list[row][col].add(array[nr][nc])
                            pos_hap += temp[array[nr][nc]]

            if result < pos_hap:
                result = pos_hap

print(result)

        