import sys
sys.stdin = open('성곽.txt')
import collections


def bfs_1(r, c):
    global count
    global sung


    deq = collections.deque()
    deq.append((r, c))
    cnt = 0
    visit[r][c] = 1
    while deq:
        br, bc = deq.popleft()
        temp_num = sung[br][bc]
        new_sung[br][bc] = count
        cnt += 1

        if temp_num % 2 == 1: # 서
            temp_num -= 1
        else:
            if 0 <= br < M and 0 <= bc - 1 < N:
                if new_sung[br][bc - 1] == 0 and visit[br][bc - 1] == 0:
                    visit[br][bc - 1] = 1
                    deq.append((br, bc - 1))
        
        if temp_num >= 8:  # 남
            temp_num -= 8
        else:
            if 0 <= br + 1 < M and 0 <= bc < N:
                if new_sung[br + 1][bc] == 0 and visit[br + 1][bc] == 0:
                    visit[br + 1][bc] = 1
                    deq.append((br + 1, bc))

        if temp_num >= 4:  # 동
            temp_num -= 4
        else:
            if 0 <= br < M and 0 <= bc + 1 < N:
                if new_sung[br][bc + 1] == 0 and visit[br][bc + 1] == 0:
                    visit[br][bc + 1] = 1
                    deq.append((br, bc + 1))
        
        if temp_num >= 2:  # 북
            temp_num -= 2
        else:
            if 0 <= br - 1 < M and 0 <= bc < N:
                if new_sung[br - 1][bc] == 0 and visit[br - 1][bc] == 0:
                    visit[br - 1][bc] = 1
                    deq.append((br - 1, bc))
    
    return cnt

N, M = map(int, input().split())  # N : col, M : row
sung = [list(map(int, input().split())) for _ in range(M)]
new_sung = [[0 for _ in range(N)] for _ in range(M)]
visit = [[0 for _ in range(N)] for _ in range(M)]
count = 0
room_list = [0]

for row in range(M):
    for col in range(N):

        if new_sung[row][col] == 0:
            count += 1
            room = bfs_1(row, col)
            room_list.append(room)

print(count)
print(max(room_list))
crush_max = float('-inf')

dr = [0, 1]
dc = [1, 0]

for row in range(M):
    for col in range(N):
        for w in range(2):
            nr = row + dr[w]
            nc = col + dc[w]

            if 0 <= nr < M and 0 <= nc < N:
                if new_sung[row][col] != new_sung[nr][nc]:
                    hap = room_list[new_sung[row][col]] + room_list[new_sung[nr][nc]]
                    crush_max = max(hap, crush_max)

print(crush_max)