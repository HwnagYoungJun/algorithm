import sys
sys.stdin = open('5185.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, num_16 = input().split()
    num_16 = int(num_16, 16)
    num_16 = format(num_16, 'b')
    if len(num_16) % 4 == 1:
        num_16 = '000' + num_16
    elif len(num_16) % 4 == 2:
        num_16 = '00' + num_16
   
    elif len(num_16) % 4 == 3:
        num_16 = '0' + num_16

    print("#{} {}".format(test_case, num_16))