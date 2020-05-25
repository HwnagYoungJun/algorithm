import sys
sys.stdin = open('벌꿀채취.txt')
T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    # N : 벌통의 크기, M = 선택벌통, C = 최대량
    honey = [list(map(int, input().split())) for _ in range(N)]
    com_list = []
    for i in range(1, 2 ** M):
        com_list.append(list(format(i, 'b').zfill(M)))
    result = 0  
    com_list = com_list[::-1]
    sv_honey1 = -1
    sv_honey2 = -1
    temp_list = list()
    for c1 in com_list:
        for row1 in range(N):
            for col1 in range(N - M + 1):
                already_work = [[0 for _ in range(N)] for _ in range(N)]
                take_honey1 = 0
                mx_honey1 = 0
                for b1 in range(M):
                    if c1[b1] == '1':
                        mx_honey1 += honey[row1][col1 + b1]
                if mx_honey1 > C:
                    continue
                for a1 in range(M):
                    already_work[row1][col1 + a1] = 1
                    if c1[a1] == '1':
                        take_honey1 += honey[row1][col1 + a1] ** 2
                if take_honey1 <= sv_honey1:
                    continue
                else:
                    sv_honey1 = take_honey1
                    for c2 in com_list:
                        for row2 in range(N):
                            for col2 in range(N - M + 1):
                                if already_work[row2][col1] == 0:
                                    # print('1: ', row1, col1, c1)
                                    # print('2: ', row2, col2, c2)
                                    take_honey2 = 0
                                    mx_honey2 = 0
                                    for b2 in range(M):
                                        if c2[b2] == '1':
                                            mx_honey2 += honey[row2][col2 + b2]
                                            take_honey2 += honey[row2][col2 + b2] ** 2
                                    if mx_honey2 <= C:
                                        sv_honey2 = take_honey2
                                        # print('1: ', row1, col1, c1)
                                        # print('2: ', row2, col2, c2)
                                            # print(row1, col1,  mx_honey1, c1)
                                            # print(row2, col2,  mx_honey2, c2)
                                        # print(sv_honey1, sv_honey2)
                                        result = sv_honey1 + sv_honey2
                                        temp_list.append(result) 
    print('#{} {}'.format(test_case, max(temp_list)))
    