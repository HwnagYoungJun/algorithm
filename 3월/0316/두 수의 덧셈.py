import sys
sys.stdin = open('두 수의 덧셈.txt')

T = int(input())

for test_case in range(1, T + 1):
    A, B = map(int, input().split())
    C = A + B
    print("#{} {}".format(test_case, C))