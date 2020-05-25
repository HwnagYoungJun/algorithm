import sys
sys.stdin = open('최적경로.txt')
def dis(y1, x1, y2, x2):
    return abs(y1 - y2) + abs(x1 - x2)

def dfs(y, x, distance, k):
    global sv_distance
    if distance > sv_distance:
        return
    if k == N:
        result = distance + dis(y, x, zip_x, zip_y)
        if result < sv_distance:
            sv_distance = result
        return
    for row, col in temp_list:
        if visit[row][col] == 0:
            visit[row][col] = 1
            dfs(row, col, distance + dis(y, x, row, col), k + 1)
            visit[row][col] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    location = list(map(int, input().split()))
    company_x = location[0]
    company_y = location[1]
    zip_x = location[2]
    zip_y = location[3]
    location = location[4:]
    temp_list = list()
    for i in range(0, 2 * N, 2):
        temp_list.append([location[i], location[i + 1]])
    sv_distance = float('inf')
    visit = [[0 for _ in range(101)] for _ in range(101)]
    for row, col in temp_list:
        visit[row][col] = 1
        dfs(row, col, dis(company_x, company_y, row, col), 1)
        visit[row][col] = 0
    print('#{} {}'.format(test_case, sv_distance))



