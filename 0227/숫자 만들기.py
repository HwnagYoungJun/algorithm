import sys
from itertools import permutations
sys.stdin = open('숫자 만들기.txt')
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    temp_list = list(map(int, input().split())) 
    calc_list = list() # 더하기, 빼기 등이 있는 리스트
    num_list = list(map(int, input().split()))
    for i in range(4):
        for j in range(temp_list[i]):
            if i == 0:
                calc_list.append('+')
            elif i == 1:
                calc_list.append('-')
            elif i == 2:
                calc_list.append('*')
            elif i == 3:
                calc_list.append('/')
    my_max = -100000000
    my_min = 100000000
    for i in permutations(calc_list):
        count = num_list[0]
        for j in range(N - 1):
            if i[j] == '+':
                count += num_list[j + 1]
            elif i[j] == '-':
                count -= num_list[j + 1]
            elif i[j] == '*':
                count *= num_list[j + 1]
            elif i[j] == '/':
                count /= num_list[j + 1]
                count = int(count)
        if count > my_max:
            my_max = count
        if count < my_min:
            my_min = count
    print('#{} {}'.format(test_case, my_max - my_min))