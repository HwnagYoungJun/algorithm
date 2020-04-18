import sys
sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1, T + 1):
    S1, S2 = map(str, input().split())
    S1 = list(S1)
    S2 = list(S2)
    zero_hole = ['C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'S', 'T', 'U', 'V', 'W', 'X', 'Y' ,'Z']
    one_hole = ['A', 'D', 'O', 'P', 'Q', 'R']
    two_hole = ['B']
    case_zero = 0
    case_one = 1
    case_two = 2
    len_S1 = len(S1)
    len_S2 = len(S2)
    result = 'SAME'
    if len_S1 != len_S2:
        result = 'DIFF'
    else:
        for i in range(len_S1):
            if S1[i] in zero_hole:
                S1[i] = case_zero
            elif S1[i] in one_hole:
                # print(i)
                # print(S1[i])
                # print(case_one)
                S1[i] = 1
            else:
                S1[i] = case_two
        for i in range(len_S2):
            if S2[i] in zero_hole:
                S2[i] = case_zero
            elif S2[i] in one_hole:
                S2[i] = case_one
            else:
                S2[i] = case_two
        for i in range(len_S1):
            if S1[i] != S2[i]:
                result = 'DIFF'
                break
    print('#{} {}'.format(test_case, result))