import sys
sys.stdin = open('5202.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    lst = [list(map(int, input().split())) for _ in range(N)]

    lst.sort(key=lambda x: x[1])
    end = lst[0][0]
    print(lst)
    cnt = 1
    for i in range(1, N):
        if end <= lst[i][0]:
            end = lst[i][1]
            cnt += 1

    print('#{} {}'.format(test_case, cnt))