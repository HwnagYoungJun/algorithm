import sys
import collections
sys.stdin = open('수지의 수지 맞는 여행.txt')
def bfs(row, col, k): # k = 깊이
    global result

    if k > result:
        result = k

    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if 0 <= nr < R and 0 <= nc < C:
            if island[nr][nc] not in visit:
                visit.append(island[nr][nc])
                bfs(nr, nc, k + 1)
                visit.remove(island[nr][nc])

T = int(input())

for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    island = [list(map(str ,input())) for _ in range(R)]
     deq = collections.deque()
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    result = float('-inf')
    bfs(0, 0, 1)
    print("#{} {}".format(test_case, result))