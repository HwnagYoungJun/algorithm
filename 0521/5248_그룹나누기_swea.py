import sys
sys.stdin = open('5248.txt')

def find(x):
    if x == parrent[x]:
        return x
    parrent[x] = find(parrent[x])
    return parrent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parrent[fy] = fx

T = int(input())
for test_case in range(1, T + 1):

    N, M = map(int, input().split())
    temp = list(map(int, input().split()))
    group = 0
    parrent = [i for i in range(N + 1)]
    for i in range(0, M * 2, 2):
        x = temp[i]
        y = temp[i + 1]
        if find(x) != find(y):
            union(x, y)

    for i in range(1, N + 1):
        parrent[i] = find(parrent[i])
    
    group = len(set(parrent)) - 1
    
    print("#{} {}".format(test_case, group))