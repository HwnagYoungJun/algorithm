import sys
sys.stdin = open('정사각형 방.txt')
import collections
def bfs (row, col, k):
    deq.append((row, col, k))
    while len(deq) != 0:
        br, bc, bk = deq.popleft()
        # print(br, bc, bk)
        for w in range(4):
            nr = br + dr[w]
            nc = bc + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if num_map[nr][nc] == num_map[br][bc] + 1:
                    deq.append((nr, nc, bk + 1))
    return bk

T = int(input())
for test_case in range(1 , T + 1):
    N = int(input())
    num_map = [list(map(int, input().split())) for _ in range(N)] # 입력
    dr = [0, 0, -1, 1] # 델타 로우
    dc = [-1, 1, 0, 0] # 델타 칼럼
    deq = collections.deque()
    max_move = float('-inf')
    dap_save = float('inf')
    for row in range(N):
        for col in range(N):
            # print('row, col : ', row, col)
            save = num_map[row][col] # 출발한 곳의 정보저장
            result = bfs(row, col, 1)
            if result > max_move:
                max_move = result
                dap_save = save
            elif result == max_move:
                if save < dap_save:
                    dap_save = save
    print('#{} {} {}'.format(test_case, dap_save, max_move))