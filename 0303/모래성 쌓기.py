import sys
sys.stdin = open('모래성 쌓기.txt')
import collections
 
T = int(input())
for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    sand_castle = [list(map(str, input())) for _ in range(R)]
    castle_cnt = [[0 for _ in range(C)] for _ in range(R)]
    dr = [0, 0, 1, -1, 1, -1, 1, -1]
    dc = [-1, 1, 0, 0, 1, -1, -1, 1]
    deq = collections.deque()
    for row in range(1, R - 1):
        for col in range(1, C - 1):
            if sand_castle[row][col].isdigit() == True:
                count = 0
                sand_castle[row][col] = int(sand_castle[row][col])
                for w in range(8):
                    nr = row + dr[w]
                    nc = col + dc[w]
                    if sand_castle[nr][nc] == '.':
                        count += 1
                castle_cnt[row][col] = count
                if count >= sand_castle[row][col]:
                    deq.append((row, col))
     
    pado = 0
    while len(deq) != 0:
        pado += 1
        for i in range(len(deq)):
            br, bc = deq.popleft()
            sand_castle[br][bc] = '.'
            for w in range(8):
                nr = br + dr[w]
                nc = bc + dc[w]
                castle_cnt[nr][nc] += 1
                if sand_castle[nr][nc] != '.' and castle_cnt[nr][nc] == sand_castle[nr][nc]:
                    deq.append((nr, nc))
 
    print('#{} {}'.format(test_case, pado))