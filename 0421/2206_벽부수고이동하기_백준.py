import sys
sys.stdin = open('2206.txt')
import collections
input = sys.stdin.readline

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs():
    deq = collections.deque()
    deq.append((0, 0, True, 1))
 
    visit = [[[0, 0] for _ in range(M)] for _ in range(N)]
    visit[0][0] = [1, 1]
    while deq:
        row, col, status, cnt = deq.popleft()

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < N and 0 <= nc < M:
                if status == False:  # 벽을 부숨
                    if visit[nr][nc][1] == 0 and mapmap[nr][nc] == 0:
                        if (nr, nc) == (N - 1, M - 1):
                            return cnt + 1
                        else:
                            visit[nr][nc][1] = 1 
                            deq.append((nr, nc, status, cnt + 1))
                else:  # 벽을 안부숨
                    if visit[nr][nc][0] == 0:
                        if (nr, nc) == (N - 1, M - 1):
                            return cnt + 1
                        else:
                            if mapmap[nr][nc] == 0:
                                visit[nr][nc][0] = 1
                                deq.append((nr, nc, status, cnt + 1))
                            else:
                                visit[nr][nc][1] = 1
                                deq.append((nr, nc, False, cnt + 1))

    return -1


N, M = map(int, input().split())

mapmap = [list(map(int, input())) for _ in range(N)]
if N == 1 and M == 1:
    print(1)
else:
    print(bfs())