import sys
sys.stdin = open('5186.txt')

T = int(input())

for test_case in range(1, T + 1):

    N = float(input())
    result = list()
    a = 1
    while True:
        if N == 0 or a < 2**(-13):
            break
        a /= 2
        if N >= a:
            result.append('1')
            N -= a
        else:
            result.append('0')
        
    if a < 2 **(-13):
        result = 'overflow'
    else:
        result = ''.join(result)    
    print('#{} {}'.format(test_case, result))