import sys
import copy
sys.stdin = open('가능한 시험 점수.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    question = list(map(int, input().split()))
    temp_set = {0}
    for i in question:
        tt_set = copy.copy(temp_set)
        for j in tt_set:
            if 0 <= i + j < 10001: 
                temp_set.add(i + j)
    print('#{} {}'.format(test_case, len(temp_set)))