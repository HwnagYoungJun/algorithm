import sys
sys.stdin = open('16724.txt')
import collections

def peter_the_piper(r, c):
    deq = collections.deque()
    deq.append((r, c))
    foot_step = dict()
    foot_step[(r, c)] = True
    while deq:
        row, col = deq.popleft()
        d = move(map_list[row][col])
        nr = row + d[0]
        nc = col + d[1]
        if 0 <= nr < N and 0 <= nc < M:
            if foot_step.get((nr, nc)) != None:
                visit[nr][nc] = True
                safe_zone.add((nr, nc))
                return
            else:
                if visit[nr][nc]:
                    return
                else:
                    visit[nr][nc] = True
                    foot_step[(nr, nc)] = True
                    deq.append((nr, nc))

def move(D):
    if D == 'U':
        d = [-1, 0]
    elif D == 'D':
        d = [1, 0]
    elif D == 'L':
        d = [0, -1]
    else:
        d = [0, 1]

    return d

N, M = map(int, input().split())
map_list = [list(input()) for _ in range(N)]

visit = [[False for _ in range(M)] for _ in range(N)]
safe_zone = set()
for row in range(N):
    for col in range(M):
        if visit[row][col]:
            continue
        visit[row][col] = True
        peter_the_piper(row, col)
print(safe_zone)
print(len(safe_zone))