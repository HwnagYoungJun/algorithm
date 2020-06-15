import sys
sys.stdin = open('18231.txt')

N, M = map(int, input().split())
conj = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    conj[u].append(v)
    conj[v].append(u)

K = int(input())
destroy_city = list(map(int, input().split()))
already_destory = {i: True for i in destroy_city}
drop_bomb = []

for city in destroy_city:
    for conj_city in conj[city]:
        if already_destory.get(conj_city) == None:
            break
        if not already_destory[conj_city]:
            break
    else:
        drop_bomb.append(city)

if drop_bomb:
    print(*drop_bomb)
else:
    print(-1)
