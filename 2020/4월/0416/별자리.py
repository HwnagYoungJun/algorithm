import sys
sys.stdin = open('별자리.txt')
import collections

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
T = int(input())

def bfs(r, c):
    deq = collections.deque()
    star[r][c] = 1
    deq.append((r, c))

    while deq:
        br, bc = deq.popleft()

        for w in range(8):
            nr = br + dr[w]
            nc = bc + dc[w]

            if 0 <= nr < 10 and 0 <= nc < 10:
                if star[nr][nc] == 1:
                    star[nr][nc] = 0
                    deq.append((nr, nc))



for test_case in range(1, T + 1):
    
    star = [list(map(int, input().split())) for _ in range(10)]

    count = 0
    for row in range(10):
        for col in range(10):
            if star[row][col] == 1:
                count += 1
                bfs(row, col)

    print("#{} {}".format(test_case, count))