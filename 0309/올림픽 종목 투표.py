import sys
sys.stdin = open('올림픽 종목 투표.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    event = list(map(int, input().split()))
    jojik = list(map(int ,input().split()))

    vote = [0] * (N + 1)
    for i in jojik:
        chk = float('-inf')
        num_chk = 0
        for j in range(N):
            if i >= event[j]:
                chk = event[j]
                num_chk = j + 1
                break
        # print(num_chk)
        vote[num_chk] += 1
    result_chk = float('-inf')
    for i in range(1, N + 1):
        if result_chk < vote[i]:
            result_chk = vote[i]
            result = i
    print('#{} {}'.format(test_case, result))
        
