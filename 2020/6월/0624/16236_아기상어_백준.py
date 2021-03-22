import sys
sys.stdin = open('16236.txt')
import collections

# 처음 상어의 크기는 2!
# 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음.
# 자신의 크기와 같은 수의 물고기를 먹을때마다 크기가 1증가!
# -------------------------------------------------------------- #
# 1. 초기 상태를 확인한다.
# 2. 물고기를 찾는다.
# 3. 제일 가까운 물고기를 먹는다.
# 4. 반복한다.
# -------------------------------------------------------------- #

def bfs(start):
    global shark_size
    deq = collections.deque()
    deq.append((start[0], start[1]))
    visit = {(row, col): False for row in range(N) for col in range(N)}
    visit[start] = True
    fishes = []
    time = 0
    while deq:
        # 2. 물고기를 찾는다.
        for _ in range(len(deq)):
            row, col = deq.popleft()
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < N and 0 <= nc < N:
                    if visit[(nr, nc)]:
                        continue
                    if map_list[nr][nc] > shark_size[0]:
                        continue
                    visit[(nr, nc)] = True
                    if 1 <= map_list[nr][nc] < shark_size[0]:
                        fishes.append((nr, nc))
                        
                    else:
                        deq.append((nr, nc))
                
        time += 1
        # 3. 물고기를 먹는다.
        if fishes:
            best_fish = [INF, INF]
            for fish in fishes:
                if fish[0] < best_fish[0]:
                    best_fish = fish
                elif fish[0] == best_fish[0]:
                    if fish[1] < best_fish[1]:
                        best_fish = fish
            
            map_list[best_fish[0]][best_fish[1]] = 0
            if shark_size[0] == shark_size[1] + 1:
                shark_size = [shark_size[0] + 1, 0]
            else:
                shark_size[1] += 1
            return (time, best_fish)
    
    # 물고기를 못먹었어.. ㅠㅠ
    return (0, 0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = float('inf')

N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]
shark_size = [2, 0] # [(크기), (먹은물고기의수)]

# 1. 초기상태를 확인한다.
for row in range(N):
    for col in range(N):
        if map_list[row][col] == 9:
            start = (row, col)
            map_list[row][col] = 0

time = 0
while True:
    eat_time, next_start = bfs(start)
    if eat_time != 0:
        time += eat_time
        start = next_start
        # 4. 반복한다.
    else:
        break

print(time)