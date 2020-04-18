import sys
sys.stdin = open('벌꿀채취.txt')
T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    # N : 벌통의 크기, M = 선택벌통, C = 최대량
    honey = [list(map(int, input().split())) for _ in range(N)]
    result_list = list()
    for collect1 in range(M, 0, -1):
        for row1 in range(N):
            for col1 in range(N - collect1 + 1):
                already_work = [[0 for _ in range(N)] for _ in range(N)]
                take_honey_1 = 0
                for i in range(collect1):
                    take_honey_1 += honey[row1][col1 + i]
                    already_work[row1][col1 + i] = 1
                if take_honey_1 <= C:   
                    for row2 in range(N):
                        for col2 in range(col1, N - M + 1):
                            take_honey_2 = 0
                            result = 0
                            if already_work[row2][col2] == 0:
                                # print(row1, col1)
                                # print(row2, col2)
                                # print()
                                for j in range(M):
                                    take_honey_2 += honey[row2][col2 + j]
                                if take_honey_2 <= C:
                                    for z in range(M):
                                        result += honey[row1][col1 + z] ** 2 + honey[row2][col2 + z] ** 2
                                        if result == 234:
                                            print(row1, col1, row2, col2, collect1)
                                        result_list.append(result)
    print(result_list)
    print('#{} {}'.format(test_case, max(result_list)))
