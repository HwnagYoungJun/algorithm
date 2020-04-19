import sys
sys.stdin = open('1261.txt')
import collections 

def dijkstra():

    dijk = [[float('inf') for _ in range(M)] for _ in range(N)]
    dijk[0][0] = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    row = 0
    col = 0
    temp_set = set()
    while True:
        
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
        
            if 0 <= nr < N and 0 <= nc < M:
                if miro[nr][nc] == 1 and visit[nr][nc] == 0:
                    weight = 1
                else:
                    weight = 0
                
                via = dijk[row][col] + weight
                if via < dijk[nr][nc]:
                    dijk[nr][nc] = via 
                    temp_set.add((nr, nc))

        visit[row][col] = 1
        min_distance = float('inf')
        for r, c in temp_set:
            if visit[r][c] == 0 and min_distance > dijk[r][c]:
                min_distance = dijk[r][c]
                row = r
                col = c 
        

        if visit[row][col]:
            break
        temp_set.remove((row, col))

    return dijk[N - 1][M - 1]
                 
                
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

M, N = map(int, input().split())

miro = [list(map(int, input())) for _ in range(N)]

print(dijkstra())
 