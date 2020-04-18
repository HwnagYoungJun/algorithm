from collections import deque
import sys
sys.stdin = open('최적경로.txt')

def dist(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

def dfs(ny, nx, l, cnt):
    global minlength
    if l > minlength: 
        return
    if cnt == N:
        result = l + dist(ny, nx, jip[0], jip[1])
        if result < minlength:
            minlength = result
        return
    for i, j in gogeks:
        if visit[i][j] is False:
            visit[i][j] = True
            dfs(i, j, l + dist(ny, nx, i, j), cnt +1)
            visit[i][j] = False
 
t = int(input())
 
for _t in range(1, t+1):
 
    N = int(input())
 
    position_input = list(map(int, input().split()))
 
    hoesa = position_input[:2]
    jip = position_input[2:4]
    temp = position_input[4:]
    gogeks= []
    for idx, val in enumerate(temp):
        if idx %2 == 0:
            gogeks.append((val, temp[idx+1]))
 
    visit = [[False for i in range(101)] for j in range(101)]
 
    minlength = float('inf')
 
    for i, j in gogeks:
        visit[i][j] = True
        dfs(i, j, dist(*hoesa, i, j), 1)
        visit[i][j] = False
 
    print('#{} {}'.format(_t, minlength))