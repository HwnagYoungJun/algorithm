import sys
sys.stdin = open('동철이의 일분배.txt')
def perm(k, result_percentage):
    global result
    if result >= result_percentage:
        return
    if k == N - 1:
        result = result_percentage
        return
    for w in range(N):
        if visit[w] == 0:
            visit[w] = 1
            perm(k + 1, result_percentage * percent[w][k + 1])
            visit[w] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    for row in range(N):
        for col in range(N):
            percent[row][col] /= 100
    visit = [0 for _ in range(N)]
    result = float('-inf')
    for i in range(N):
        visit[i] = 1
        perm(0, percent[i][0])
        visit[i] = 0
    result *= 100
    result = format(result, '0.6f')
    print('#{} {}'.format(test_case, result))


