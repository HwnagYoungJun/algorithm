import sys
sys.stdin = open('늘어지는 소리 만들기.txt')

T = int(input())
for test_case in range(1, T + 1):
    munja = list(input())
    N = len(munja)
    H = int(input())
    input_witch = list(map(int, input().split()))
    witch_list = [''] * (N + 1)
    for i in input_witch:
        witch_list[i] += '-'
    
    print("#{} ".format(test_case),end='')
    for i in range(N):
        result = witch_list[i] + munja[i]
        print("{}".format(result), end='')
    print("{}".format(witch_list[N]))
