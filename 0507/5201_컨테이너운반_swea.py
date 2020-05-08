import sys
sys.stdin = open('5201.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # N : 컨테이너 수, M : 트럭 수

    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    freights.sort()
    trucks.sort()

    result = 0
    
    for i in range(len(trucks) - 1, - 1, -1):
        truck = trucks[i]
        while freights:
            a = freights.pop()
            if truck >= a:
                result += a
                break    

    print("#{} {}".format(test_case, result))