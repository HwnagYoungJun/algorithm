import sys
sys.stdin = open('1486.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    result = []
    for i in range(1, 1 << N):
        h = 0
        for j in range(N):
            if i & (1 << j):
                h += heights[j]
            if h >= B:
                result.append(h)
                break
    result.sort()
    print('#{} {}'.format(test_case, result[0] - B))