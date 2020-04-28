import sys
sys.stdin = open('2668.txt')

def dfs(v, i):
    global result
    visit[v] = 1
    print(v, i)
    nex = grape[v]

    if visit[nex] == 0:
        dfs(nex, i)
    elif visit[nex] == 1 and nex == i:
        result.append(nex)




N = int(input())
grape = [0 for i in range(N + 1)]
for i in range(N):
    grape[i + 1] = int(input())

result = []

for i in range(1, N + 1):
    visit = [0 for _ in range(N + 1)]
    dfs(i, i)

print(len(result))
for i in result:
    print(i)