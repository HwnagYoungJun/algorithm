import sys
from itertools import combinations
sys.stdin = open('요리사.txt')
# def my_combi():

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    N2 = int(N / 2)
    food = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    for i in range(1, 2 ** N):
        combi = list(format(i, 'b').zfill(N))
        if combi.count('1') == N2:
            A_synergy = 0
            B_synergy = 0
            A_list = list()
            B_list = list()
            for j in range(N):
                if combi[j] == '1':
                    A_list.append(j)
                else:
                    B_list.append(j)
            for p in range(N2 - 1):
                for q in range(p + 1, N2):
                    A_synergy += food[A_list[p]][A_list[q]] + food[A_list[q]][A_list[p]]
                    B_synergy += food[B_list[p]][B_list[q]] + food[B_list[q]][B_list[p]]
            if abs(A_synergy - B_synergy) < result:
                result = abs(A_synergy - B_synergy)            
    print('#{} {}'.format(test_case, result))
                
            


                    