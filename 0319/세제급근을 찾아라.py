import sys
sys.stdin = open("세제곱근을 찾아라.txt")

T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    if num % 2 == 1:
        for i in range(1, 10 ** 6 + 1, 2):
            if i ** 3 == num:
                x = i
                break
        else:
            x = -1
    else:
        for i in range(2, 10 ** 6 + 1, 2):
            if i ** 3 == num:
                x = i
                break
        else:
            x = -1
    print("#{} {}".format(test_case, x))

