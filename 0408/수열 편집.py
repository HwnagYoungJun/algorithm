import sys
sys.stdin = open('수열 편집.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M, L = map(int ,input().split())

    my_list = list(map(int, input().split()))

    for _ in range(M):
        temp = list(input().split())

        if temp[0] == 'I':
            index = int(temp[1])
            vaule = int(temp[2])
            my_list.insert(index, vaule)
        elif temp[0] == 'D':
            index = int(temp[1])
            my_list.pop(index)
        elif temp[0] == 'C':
            index = int(temp[1])
            vaule = int(temp[2])
            my_list[index] = vaule
    if L >= len(my_list):
        result = -1

    else:
        result = my_list[L]
    print("#{} {}".format(test_case, result))
