# import sys
# sys.stdin = open("input.txt")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nong_list = [list(map(int, input())) for _ in range(N)]
    # print(nong_list)
    point_N = int(N / 2)
    benefit = 0
    i = 0
    for row in range(N):
        if row < point_N + 1:
                for col in range(point_N - row, point_N + row + 1):
                    # print(row, col)
                    benefit += nong_list[row][col]

        else:
            for col in range(point_N + row - N + 1, point_N - row + N):
                # print(row, col)
                benefit += nong_list[row][col]
    print('#{} {}'.format(test_case, benefit))
    