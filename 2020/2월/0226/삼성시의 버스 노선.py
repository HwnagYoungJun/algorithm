import sys
sys.stdin = open('삼성시의 버스 노선.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    no_sun = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stop = list()
    for i in range(P):
        bus_stop.append(int(input()))
    max_bus = max(bus_stop)
    temp_list = [0] * (5001)

    for row in range(N):
        for i in range(no_sun[row][0], no_sun[row][1] + 1):
            temp_list[i] += 1
    print('#{}'.format(test_case),end=' ')
    for i in bus_stop:
        if i == bus_stop[-1]:
            print(temp_list[i])
        else:
            print(temp_list[i], end= ' ')