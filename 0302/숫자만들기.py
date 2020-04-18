import sys
sys.stdin = open('숫자만들기.txt')
def fx(n, k, plus, minus, multiple, division, result):
    global big_data, small_data
    if n == k:
        # print(result)
        if result > big_data:
            big_data = result
        if result < small_data:
            small_data = result
        return
    else:
        if plus > 0:
            fx(n, k + 1, plus - 1, minus, multiple, division, result + num_list[k])
        if minus > 0:
            fx(n, k + 1, plus, minus - 1, multiple, division, result - num_list[k])
        if multiple > 0:
            fx(n, k + 1, plus, minus, multiple - 1, division, result * num_list[k])
        if division > 0:
            fx(n, k + 1, plus, minus, multiple, division - 1, int(result / num_list[k]))

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    temp_list = list(map(int, input().split())) 
    # calc_list = list() # 더하기, 빼기 등이 있는 리스트
    num_list = list(map(int, input().split()))
    # for i in range(4):
    #     for j in range(temp_list[i]):
    #         if i == 0:
    #             calc_list.append('+')
    #         elif i == 1:
    #             calc_list.append('-')
    #         elif i == 2:
    #             calc_list.append('*')
    #         elif i == 3:
    #             calc_list.append('/')
    big_data = float('-inf')
    small_data = float('inf')
    fx(N, 1, temp_list[0], temp_list[1], temp_list[2],temp_list[3], num_list[0])
    print('#{} {}'.format(test_case, big_data - small_data))
