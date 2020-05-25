import sys
sys.stdin = open('말이 되고픈 원숭이.txt')
import collections

def bfs():
    deq = collections.deque()
    deq.append((0, 0, 0, 0))
    visit = [[[0 for _ in range(K + 1)] for _ in range(W)] for _ in range(H)]

    while deq:
        br, bc, bk, bcnt = deq.popleft()
        
        if br == H - 1 and bc == W - 1:
            return bk
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < H and 0 <= nc < W:
                if travel_road[nr][nc] == 0 and visit[nr][nc][bcnt] == 0:
                    visit[nr][nc][bcnt] = 1
                    deq.append((nr, nc, bk + 1, bcnt))  

        if bcnt < K:
            for w in range(8):
                nr = br + horse_dr[w]
                nc = bc + horse_dc[w]
                if 0 <= nr < H and 0 <= nc < W:
                    if travel_road[nr][nc] == 0 and visit[nr][nc][bcnt + 1] == 0:
                        visit[nr][nc][bcnt + 1] = 1
                        deq.append((nr, nc, bk + 1, bcnt + 1))

    return -1

K = int(input())
W, H = map(int, input().split())
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
horse_dr = [-1, -2, -2, -1, 1, 2, 2, 1]
horse_dc = [-2, -1, 1, 2, 2, 1, -1, -2]
travel_road = [list(map(int, input().split())) for _ in range(H)]
print(bfs())