import sys
sys.stdin = open('경로 찾기.txt')
import collections
def bfs(s, e):
    global result
    deq = collections.deque()
    deq.append(s)
    visit = [0 for _ in range(N)]
    while deq:
        st = deq.popleft()
        for col in range(N):
            if grape[st][col] == 1 and visit[col] == 0:
                if col == e:
                    return 1
                else:
                    visit[col] = 1
                    deq.append(col)
    return 0

N = int(input())

grape = [list(map(int ,input().split())) for _ in range(N)]

result = [[0 for _ in range(N)] for _ in range(N)]

for start in range(N):
    for end in range(N):
        
        a = bfs(start, end)

        if a == 1:
            result[start][end] = 1

for i in result:
    print(*i)