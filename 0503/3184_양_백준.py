import sys
sys.stdin = open('3184.md')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(r, c):
    global madang
    wolf_count = 0  
    sheep_count = 0
    deq = collections.deque()
    deq.append((r, c))
    if madang[r][c] == 'v':
        wolf_count += 1
    elif madang[r][c] == 'o':
        sheep_count += 1
    madang[r][c] = area
  
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < R and 0 <= nc < C:
                if madang[nr][nc] == '.' or madang[nr][nc] == 'v' or madang[nr][nc] == 'o':
                    if madang[nr][nc] == '.':
                        pass    
                    elif madang[nr][nc] == 'v':
                        wolf_count += 1
                    elif madang[nr][nc] == 'o':
                        sheep_count += 1
                    
                    madang[nr][nc] = area
                    deq.append((nr, nc))

    return sheep_count, wolf_count                


R, C = map(int, input().split())

madang = [list(input()) for _ in range(R)]

sheep = list()
wolf = list()

area = 0
for row in range(R):
    for col in range(C):
        if madang[row][col] == '.' or madang[row][col] == 'v' or madang[row][col] == 'o':
            area += 1    
            s_cnt, w_cnt = bfs(row, col)
            sheep.append(s_cnt)
            wolf.append(w_cnt)

result_sheep = 0
result_wolf = 0

for i in range(len(sheep)):
    if sheep[i] > wolf[i]:
        result_sheep += sheep[i]
    else:
        result_wolf += wolf[i]

print(result_sheep, result_wolf)