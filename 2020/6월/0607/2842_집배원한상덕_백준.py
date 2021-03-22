import sys
sys.stdin = open('2842.txt')
import collections

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

def bfs(min_h, max_h):
    deq = collections.deque()
    deq.append(start)
    visit = {(r, c): False for r in range(N) for c in range(N)}
    visit[start] = True
    cnt = house
    while deq:
        row, col = deq.popleft()
        for w in range(8):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if min_h <= godo[nr][nc] <= max_h:
                    if not visit[(nr, nc)]:
                        visit[(nr, nc)] = True
                        if town[nr][nc] == 'K':
                            cnt -= 1
                        if cnt == 0:
                            return True
                        deq.append((nr, nc))
    
    return False

N = int(input())
town = [list(input()) for _ in range(N)]
godo = [list(map(int, input().split())) for _ in range(N)]
height_set = set()
house = 0
for r in range(N):
    for c in range(N):
        height_set.add(godo[r][c])
        if town[r][c] == 'P':
            start = (r, c)
        if town[r][c] == 'K':
            house += 1

# 투 포인터
left = 0
right = 0
can_dilivery = False
fatigue = float('inf')
height_set = list(height_set)
height_set.sort()

while True:
    min_h = height_set[left]
    max_h = height_set[right]
    if godo[start[0]][start[1]] < min_h:
        break
    elif godo[start[0]][start[1]] > max_h:
        right += 1
        continue
    can_dilivery = bfs(min_h, max_h)
    if can_dilivery:
        if max_h - min_h < fatigue:
            fatigue = max_h - min_h
            if left == right:
                break
        left += 1
    else:
        if right == len(height_set) -1:
            break 
        right += 1
print(fatigue)

