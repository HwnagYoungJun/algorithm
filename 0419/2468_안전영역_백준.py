import sys
sys.stdin = open('2468.txt')
import collections
import copy

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
# bfs
def bfs(r, c):
    global area
    deq = collections.deque()
    deq.append((r, c))
    area[r][c] = 0
    while deq:
        br, bc = deq.popleft()
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]

            if 0 <= nr < N and 0 <= nc < N:
                if area[nr][nc] > i:
                    area[nr][nc] = 0
                    deq.append((nr, nc))

        

N = int(input())

area = [list(map(int ,input().split())) for _ in range(N)]
temp_area = copy.deepcopy(area)
max_height = float('-inf')

for i in range(N):
    temp = max(area[i])
    if max_height < temp:
        max_height = temp

max_safe = float('-inf')
for i in range(0, max_height):
    count = 0
    area = copy.deepcopy(temp_area)
    for row in range(N):
        for col in range(N):
            if area[row][col] > i:
                count += 1
                bfs(row, col)
                for j in area:
                    print(*j)
                print()
                print(count)
            
    if max_safe < count:
        max_safe = count

print(max_safe)
