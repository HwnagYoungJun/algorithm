import sys
sys.stdin = open('15649.txt')

def my_perm(K, result):
    if K == M:
        print(*result)
        return
    
    for i in range(1, N + 1):
        if visit[i] == 0:
            visit[i] = 1
            my_perm(K + 1, result + [i])
            visit[i] = 0


N, M = map(int, input().split())
visit = {i: False for i in range(N + 1)}
my_perm(0, [])