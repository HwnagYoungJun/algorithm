import sys
sys.stdin = open('6087.txt')
import collections
gr = [0, 0]
gc = [-1 , 1]

sr = [-1, 1]
sc = [0, 0]

def find_razer():
    global razer

    for row in range(R):
        for col in range(C):
            if room[row][col] == 'C':
                razer.append((row, col))
                if len(razer) == 2:
                    return
    return

def bfs():
    deq = collections.deque()
    # (row, col, mirror, status)
    deq.append((razer[0][0], razer[0][1], 0, 1))
    visit = [[[float('inf'), float('inf')] for _ in range(C)] for _ in range(R)]
    visit[razer[0][0]][razer[0][1]] = [float('-inf'), float('-inf')]

    while deq:
        row, col, mirror, status = deq.popleft()
        
        if (row, col) != razer[1] and mirror < min(visit[razer[1][0]][razer[1][1]]):

            # 1. 가로로 쏘기
            for w in range(2):
                nr = row + gr[w]
                nc = col + gc[w]
                if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != '*':
                    if visit[nr][nc][0] > mirror:
                        if status == 1:
                            nm = mirror
                        elif status == 2 :
                            nm = mirror + 1
                        visit[nr][nc][0] = nm
                        deq.append((nr, nc, nm, 1))

            # 2. 세로로 쏘기
            for w in range(2):
                nr = row + sr[w]
                nc = col + sc[w]
                if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != '*':
                    if visit[nr][nc][1] > mirror:
                        if status == 1:
                            if (row, col) == razer[0]:
                                nm = mirror
                            else:
                                nm = mirror + 1
                        elif status == 2:
                            nm = mirror
                        visit[nr][nc][1] = nm
                        deq.append((nr, nc, nm, 2))
    return min(visit[razer[1][0]][razer[1][1]])

C, R = map(int, input().split())
room = [list(input()) for _ in range(R)]

razer = []
find_razer()
# 찾고나니깐 굳이 찾을필요는 없었던것 같지만 굳이 쓴다.

print(bfs())
