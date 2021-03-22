import sys
sys.stdin = open("숨바꼭질4.txt")
import collections

def bfs(x, time, result_list):
    deq.append((x, time, result_list))
    visit[x] = 1
    while len(deq) != 0:
        bx, btime, bresult = deq.popleft()
        if bx == K:
            return btime, bresult
        temp_list = [bx, 1, -1]
        for w in range(len(temp_list)):
            nx = bx + temp_list[w]
            if 0 <= nx < 100000 + 1:
                if visit[nx] == 0 :
                    visit[nx] = 1   
                    deq.append((nx, btime + 1, bresult + [nx]))


N, K = map(int, input().split())
hide_seek = [0 for _ in range(100000 + 1)]
visit = [0 for _ in range(100000 + 1)]
deq = collections.deque()
if K < N:
    print(N - K)
    temp_list = [i for i in range(N, K - 1, -1)]
    print(*temp_list)
elif K == N:
    print(0)
    print(N)
else:
    min_time, foot_step = bfs(N, 0, [N])
    print(min_time)
    print(*foot_step)

 


