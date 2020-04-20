import sys
sys.stdin = open('6593.txt')
input = sys.stdin.readline
import collections


def se ():
    global buliding

    start = (-1, -1, -1)
    end = (-1, -1, -1)
    
    for l in range(L):
        for r in range(R):
            for c in range(C):

                if buliding[l][r][c] == 'S':
                    start = (l, r, c)
                    buliding[l][r][c] = '.'
                    if end != (-1, -1, -1):
                        return start, end
                elif buliding[l][r][c] == 'E':
                    end = (l, r, c)
                    buliding[l][r][c] = '.'
                    if start != (-1, -1, -1):
                        return start, end

    return start, end

def bfs():
    deq = collections.deque()
    a, b, c = start

    deq.append((a, b, c, 0))
    visit = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    visit[a][b][c] = 1
    min_time = float('inf')
    while deq:
        bl, br, bc, time = deq.popleft()
        print(bl, br, bc, time)
        for w in range(6):
            nr = br + dr[w]
            nc = bc + dc[w]
            nl = bl + dl[w]

            if 0 <= nr < R and 0 <= nc < C and 0 <= nl < L:
                if visit[nl][nr][nc] == 0 and buliding[nl][nr][nc] == '.':
                    if (nl, nr, nc) == end:
                        return time + 1
                    else:
                        visit[nl][nr][nc] = 1
                        deq.append((nl, nr, nc, time + 1))
    return min_time

dr = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]
dl = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())
    if (L, R, C) == (0, 0, 0):
        break
    buliding = []
    for l in range(L):
        buliding.append([list(input())[:-1] for _ in range(R)])
        a= input()

    start, end = se()

    result = bfs()

    if result == float('inf'):
        result = "Trapped!"
        print(result)
    else:
        print("Escaped in {} minute(s)".format(result))