import sys
sys.stdin = open('1717.txt')
input = sys.stdin.readline

# sys.stdin.readline을 하면 엄청빨라지는 이상한 문제

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = fx

N, M = map(int, input().split())

parent = [i for i in range(N + 1)]
answer = ['YES', 'NO']

for _ in range(M):
    mode, x, y = map(int, input().split()) 
    if mode == 0:
        union(x, y)
    elif mode == 1:
        if find(x) == find(y):
            print(answer[0])
        else:
            print(answer[1])