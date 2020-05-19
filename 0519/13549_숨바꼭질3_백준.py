import sys
sys.stdin = open('13549.txt')
import collections

dx = [-1, 1]

def findK(N, K):

    deq = collections.deque()
    deq.append((0 ,N))
    limit = K * 2
    visit = [-1] * (limit + 1)
    visit[N] = 0
    min_time = float('inf')

    while deq:
        time, location = deq.popleft()

        if time > min_time:
            continue
        
        if location == K:
            if visit[K] > time:
                min_time = time
            continue
    
        for w in range(2):
            nx = location + dx[w]
            if w == 0:
                if nx < 0:
                    continue
            else:
                if nx > limit:
                    continue
            if visit[nx] == -1 or time + 1 < visit[nx]:
                visit[nx] = time + 1
                deq.append((time + 1, nx))

        nx = location * 2
        if nx <= limit and (visit[nx] == -1 or time < visit[nx]):
            visit[nx] = time
            deq.append((time, nx))

    return visit[K]

N, K = map(int, input().split())

if N > K:
    print(N - K)
elif N == K:
    print(0)
else:
    print(findK(N, K))