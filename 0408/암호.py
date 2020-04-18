import sys
sys.stdin = open('암호.txt')

T = int(input())
for test_case in range(1, T + 1):
    # N : 처음 암호 길이, M :  K 회 반복
    N, M, K = map(int ,input().split())
    password = list(map(int, input().split()))
    index = 0
    for _ in range(K):
        index += M
        if index > N:
            index %= N
        if index == N:
            password.append(password[0] + password[-1])
        else:
            front = password[:index]
            back = password[index:]
            password = front + [front[-1] + back[0]] + back
        N += 1
    print("#{}".format(test_case), *((password[::-1])[:10]))