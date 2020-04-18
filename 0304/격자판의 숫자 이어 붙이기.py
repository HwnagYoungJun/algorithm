import collections
import sys
sys.stdin = open('격자판의 숫자 이어 붙이기.txt')
def bfs(row, col, k, string):
    global count
    global save_list
    temp_set = set()
    deq.append((row, col, k, string))
    temp_bk = 1
    while len(deq) != 0:
        br, bc, bk, bstring = deq.popleft()
        if bk != temp_bk:
            temp_set.clear()
            if bk == 7:
                save_list.add(bstring) 
                continue
        temp_bk = bk
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if (nr, nc, bstring) not in temp_set:
                    temp_set.add((nr, nc, bstring))
                    deq.append((nr, nc, bk + 1, bstring + pan[nr][nc]))
                    
T = int(input())
for test_case in range(1, T + 1):
    pan = [list(map(str, input().split())) for _ in range(4)]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    deq = collections.deque()
    save_list = set()
    for row in range(4):
        for col in range(4):
            count = 0
            bfs(row, col, 1, pan[row][col])
    print("#{} {}".format(test_case, len(save_list)))