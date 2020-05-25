import sys
sys.stdin = open("운동.txt")

def dfs(r, root, hap_dis):
    global min_distance
    if min_distance < hap_dis:
        return
    if r == root and hap_dis != 0:
        min_distance = hap_dis
        return
    
    for col in range(1, N + 1):
        if load_map[r][col] != 0 and visit[col] == 0:
            visit[col] = 1
            dfs(col, root, hap_dis + load_map[r][col])
            visit[col] = 0


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N개의 건물, M개의 도로
    load_map = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    min_distance = float('inf')
    for case in range(M):
        building1, buliding2, distance = map(int, input().split())
        load_map[building1][buliding2] = distance

    for row in range(1, N + 1):
        visit = [0 for _ in range(N + 1)]
        dfs(row, row, 0)

    print("#{} {}".format(test_case, min_distance))


