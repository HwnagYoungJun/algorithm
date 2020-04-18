import sys
sys.stdin = open("치즈.txt")
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(row, col):
    global is_true
    visit = [[0 for _ in range(C)] for _ in range(R)]

    for w in range(4):
        nr = row + dr[w]
        nc = col + dc[w]
        if visit[nr][nc] == 0:
            if nr == 0 or nc == 0 or nr == R - 1 or nc == C - 1:
                is_true = False
                visit = [[1 for _ in range(C)] for _ in range(R)]
                return
            else:
                visit[nr][nc] = 1
                dfs(nr, nc)
        
def bfs():
    global is_true
    deq = collections.deque()
    for row in range(1, R - 1):
        for col in range(1, C - 1):
            if cheeze_board[row][col] == 1:
                deq.append((row, col, k))

                while len(deq) != 0:
                    is_true = True
                    br, bc, k = deq.popleft()
                    dfs(br, bc)
                    
                    

R, C = map(int, input().split())
cheeze_board = [list(map(int, input().split())) for _ in range(R)]
is_true = True
