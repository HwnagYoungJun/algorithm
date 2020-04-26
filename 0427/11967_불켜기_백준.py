import sys
sys.stdin = open('11967.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
def bfs():
    deq = collections.deque()
    deq.append((1, 1))
    visit = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    visit[1][1] = 1
    result = 1
    while deq:
        row, col = deq.popleft()
        # print(row, col, on)
        # 1. 불켜기
        for w in range(len(on_off[row][col])):
            r, c = on_off[row][col][w]
            # print(r, c)
            if room[r][c] == 0:
                result += 1
                room[r][c] = 1
            visit = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        
        on_off[row][col].clear()
        # for i in room:
        #     print(*i)

        # 2. 이동하기
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 1 <= nr < N + 1 and 1 <= nc < N + 1 and visit[nr][nc] == 0:
                if room[nr][nc] == 1:
                    visit[nr][nc] = 1
                    deq.append((nr, nc))
        
    return result


N, M = map(int, input().split())

room = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
on_off = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
room[1][1] = 1

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())

    on_off[r1][c1].append((r2, c2))

print(bfs())