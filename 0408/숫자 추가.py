import sys
sys.stdin = open('숫자 추가.txt')

T = int(input())

for test_case in range(1, T + 1):

    N, M, L = map(int, input().split())
    
    num_list = list(map(int, input().split()))
    
    for i in range(M):
        index, number = map(int ,input().split())
        front = num_list[:index]
        back = num_list[index:]
        num_list = front + [number] + back
    
    print("#{} {}".format(test_case, num_list[L]))