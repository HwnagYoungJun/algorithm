import sys
sys.stdin = open('2194.txt')
import collections


def can_go(r, c):
    for row in range(r, r + A):
        if row < 0 or row >= N:
                return False
        for col in range(c, c + B):
            if col < 0 or col >= M:
                return False
            
            if map_list[row][col] == 1:
                return False
    
    return True

def bfs():
    deq = collections.deque()
    deq.append(start)
    visit = {(row, col): False for row in range(N) for col in range(M)}
    visit[start] = True
    time = 0
    while deq:
        for _ in range(len(deq)):
            row, col = deq.popleft()
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if not can_go(nr, nc):
                    continue

                if visit[(nr, nc)]:
                    continue
                if (nr, nc) == end:
                    return time + 1
                visit[(nr, nc)] = True
                deq.append((nr, nc))

        time += 1
                
    return -1


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N, M, A, B, K = map(int, input().split())
map_list = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    map_list[r - 1][c - 1] = 1
s_r, s_c = map(int, input().split())
start = (s_r - 1, s_c - 1)
e_r, e_c = map(int, input().split())
end = (e_r - 1, e_c - 1)
print(bfs())