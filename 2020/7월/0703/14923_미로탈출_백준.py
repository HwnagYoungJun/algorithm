import sys
sys.stdin = open('14923.txt')
import collections


def bfs():

    deq = collections.deque()
    deq.append((start[0], start[1], 0))
    visit = {(r, c): [False, False] for c in range(M) for r in range(N)}
    visit[(start)] = [True, True]
    time = 0

    while deq:

        for _ in range(len(deq)):
            row, col, mode = deq.popleft()

            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]

                if 0 <= nr < N and 0 <= nc < M:

                    if mode == 0:
                        # 벽을 부수지 않았다면 벽을 부순 것보다 항상 우수하다.
                        if (nr, nc) == end:
                            return time + 1
                        
                        if miro[nr][nc] == 0:
        
                            if visit[(nr, nc)][0]:
                                continue
                            visit[(nr, nc)] = [True, True]
                            deq.append((nr, nc, 0))
                            
                        else:
                            if visit[(nr, nc)][1]:
                                continue
                            visit[(nr, nc)][1] = True
                            deq.append((nr, nc, 1))
                    
                    else:
                        if miro[nr][nc] == 0:
                            if (nr, nc) == end:
                                return time + 1
                            if visit[(nr, nc)][1]:
                                continue
                            visit[(nr, nc)][1] = True
                            deq.append((nr, nc, 1))

        time += 1

    return -1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M = map(int, input().split())
sr, sc = map(int, input().split())
start = (sr - 1, sc - 1)
er, ec = map(int, input().split())
end = (er - 1, ec  - 1)
miro = [list(map(int, input().split())) for _ in range(N)]

print(bfs())

