import sys
sys.stdin = open('5427.txt')
import collections

def bfs():
    global fire
    deq = collections.deque()
    a, b = start
    deq.append((a, b, 0))
    sv = -1
    while deq:
        row, col, time = deq.popleft()
        
        if time != sv:

            for _ in range(len(fire)):
                fr, fc = fire.popleft()
                
                for w in range(4):
                    fnr = fr + dr[w]
                    fnc = fc + dc[w]
                    if 0 <= fnr < R and 0 <= fnc < C:
                        if buliding[fnr][fnc] != '*' and buliding[fnr][fnc] != '#':
                            buliding[fnr][fnc] = '*'
                            fire.append((fnr, fnc))

        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < R and 0 <= nc < C:
                if buliding[nr][nc] == '.':
                    if nr == 0 or nr == R - 1 or nc == 0 or nc == C - 1:
                        return time + 2
                    else:
                        buliding[nr][nc] = time + 1
                        deq.append((nr, nc, time + 1))

        sv = time

    return 'IMPOSSIBLE'


dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


T = int(input())

for test_case in range(1, T + 1):

    C, R = map(int ,input().split())
    buliding = [list(input()) for _ in range(R)]
    fire = collections.deque()
    end = 1101

    for r in range(R):
        for c in range(C):
            if buliding[r][c] == '*':
                fire.append((r, c)) 
            elif buliding[r][c] == '@':

                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    end = 1
                else:
                    start = (r, c)
                    buliding[r][c] = 0
    if end == 1:
        print(1)
    else:
        print(bfs())

    