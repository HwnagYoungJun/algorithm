import sys
sys.stdin = open('1726.txt')
import collections

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs():
    deq = collections.deque()
    deq.append((sr, sc, sd, 0))
    visit = [[[0, 0, 0, 0] for _ in range(M)] for _ in range(N)]
    visit[sr][sc][sd] = 1

    while deq:
        row, col, direc, time = deq.popleft()
        # command 1.
        for w in range(1, 4):
            nr = row + dr[direc] * w
            nc = col + dc[direc] * w

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            
            dont_go = False
            for ww in range(1, w + 1):
                if factory[row + dr[direc] * ww][col + dc[direc] * ww] == 1:
                    dont_go = True
                    break

            if dont_go:
                continue

            if visit[nr][nc][direc] == 1:
                continue
            
            if (nr, nc) == (er, ec):
                v = abs(direc - ed)
                print(v)
                res = time
                if v == 0:
                    res += 1
                elif v == 1:
                    res += 2
                elif v == 2:
                    res += 3
                elif v == 3:
                    res += 2            
                return res

            visit[nr][nc][direc] = 1
            deq.append((nr, nc, direc, time + 1))

        for w in range(2):
            if w == 0:
                new_direc = turn_left(direc)
                if visit[row][col][new_direc] == 1:
                    continue
                visit[row][col][new_direc] = 1

                deq.append((row, col, new_direc, time + 1))
            else:
                new_direc = turn_right(direc)
                if visit[row][col][new_direc] == 1:
                    continue
                visit[row][col][new_direc] = 1

                deq.append((row, col, new_direc, time + 1))


def turn_left(d):

    nd = d + 1
    if nd == 4:
        nd = 0
    return nd

def turn_right(d):

    nd = d - 1
    if nd == -1:
        nd = 3
    return nd

def my_dir(d):
    if d == 1:
        d = 0
    elif d == 2:
        d = 2
    elif d == 3:
        d = 1
    elif d == 4:
        d = 3
    return d


N, M = map(int, input().split())
factory = [list(map(int, input().split())) for _ in range(N)]

sr, sc, sd = map(int, input().split())
sr -= 1
sc -= 1
sd = my_dir(sd)

er, ec, ed = map(int, input().split())
er -= 1
ec -= 1
ed = my_dir(ed)

if (sr, sc) == (er, ec):
    v = abs(sd - ed)
    res = 0
    if v == 0:
        res += 0
    elif v == 1:
        res += 1
    elif v == 2:
        res += 2
    elif v == 3:
        res += 1  

    print(res)
# 방향 별 방문체크
else:
    print(bfs())