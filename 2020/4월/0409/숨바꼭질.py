import sys
sys.stdin = open('숨바꼭질.txt')
import collections

def bfs(x, time):
    deq.append((x, time))
    visit[x] = 1
    while len(deq) != 0:
        bx, btime = deq.popleft()
        if bx == K:
            return btime
        temp_list = [bx, 1, -1]
        for w in range(len(temp_list)):
            nx = bx + temp_list[w]
            if 0 <= nx < 100000 + 1:
                if visit[nx] == 0 :
                    visit[nx] = 1   
                    deq.append((nx, btime + 1))


N, K = map(int, input().split())
hide_seek = [0 for _ in range(100000 + 1)]
visit = [0 for _ in range(100000 + 1)]
deq = collections.deque()
if K < N:
    print(N - K)
elif K == N:
    print(0)
else:
    min_time = bfs(N, 0)
    print(min_time)