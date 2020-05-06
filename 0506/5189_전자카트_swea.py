import sys
sys.stdin = open('5189.txt')
from itertools import permutations

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    golf = [list(map(int, input().split())) for _ in  range(N)]

    min_cost = float('inf')
    for i in permutations(range(1, N), N - 1):
        my_perm = [0] + list(i)
        my_perm.append(0)
        hap = 0
        for j in range(N + 1 - 1):
            hap += golf[my_perm[j]][my_perm[j + 1]]
            if hap >= min_cost:
                break
        else:
            min_cost = hap

    print('#{} {}'.format(test_case, min_cost))
