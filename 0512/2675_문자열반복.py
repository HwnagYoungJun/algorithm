import sys
sys.stdin = open('2675.txt')

T = int(input())
for test_case in range(1, T + 1):
    R, S = input().split()
    R = int(R)
    result = ''
    for i in S:
        result += i * R

    print(result)