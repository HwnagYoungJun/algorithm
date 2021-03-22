from collections import deque
import sys
sys.stdin = open('모래성 쌓기.txt')
t = int(input())
 
dy = [1, -1, 0, 0, 1, 1, -1, -1]
dx = [0, 0, 1, -1, 1, -1, 1, -1]
 
for _t in range(1, t+1):
 
    H, W = map(int, input().split())
    tilelist = deque()
 
    castle = [list(input()) for i in range(H)]
    castleCnt = [[0 for i in range(W)] for j in range(H)]
    for i in range(H):
        for j in range(W):
            if castle[i][j] != '.':
                cnt = 0
                castle[i][j] = int(castle[i][j])
                for mode in range(8):
                    newi = i + dy[mode]
                    newj = j + dx[mode]
                    if castle[newi][newj] == '.':
                        cnt += 1
                castleCnt[i][j] = cnt
                if cnt >= castle[i][j]:
                    tilelist.append((i, j))
 
    waveCnt = 0
    while tilelist:
        waveCnt += 1
        for _ in range(len(tilelist)):
            (i, j) = tilelist.popleft()
            castle[i][j] = '.'
            for mode in range(8):
                newi = i + dy[mode]
                newj = j + dx[mode]
                castleCnt[newi][newj] += 1
                if castle[newi][newj] != '.' and castleCnt[newi][newj] == castle[newi][newj]:
                    tilelist.append((newi, newj))
     
    print('#{} {}'.format(_t, waveCnt))