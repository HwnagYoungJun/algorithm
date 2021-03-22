def my_perm(k, samdae):
    global cnt
    if samdae < 500:
        return
    
    if k == N:
        cnt += 1
        return

    for i in range(len(kits)):
        if visit[i] == 0:
            visit[i] = 1
            my_perm(k + 1, samdae - K + kits[i])
            visit[i] = 0


N, K = map(int, input().split())

kits = list(map(int, input().split()))

cnt = 0
visit = [0 for _ in range(N)]
my_perm(0, 500)
print(cnt)