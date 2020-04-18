import sys
sys.stdin = open('입국심사.txt')

T = int(input())

for test_case in range(1, T + 1):
    # N : 심사대의 수, M : 사람의 수
    N, M = map(int, input().split()) 
    judgement = list()
    for i in range(N):
        a = int(input())
        judgement.append([a, a])
    judgement.sort()
    time = 0
    for i in range(M):
        temp_num = judgement.index(min(judgement))
        judgement[temp_num][0] += judgement[temp_num][1]
        
        print(judgement)
    print("#{} {}".format(test_case, max(judgement[0] - judgement[1])))