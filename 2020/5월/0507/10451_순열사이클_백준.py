import sys
sys.stdin = open('10451.txt')
import collections
def bfs(z):
    global visit
    
    deq = collections.deque()
    deq.append(z)

    while deq:
        ind = deq.popleft()
        next_index = temp[ind]
        
        if visit[next_index] == 0:
            visit[next_index] = 1
            deq.append(next_index)

    return

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    temp = list(map(int, input().split()))
    temp = [0] + temp

    visit = [0 for _ in range(N + 1)]
    cnt = 0

    for index in range(1, N + 1):
        if visit[index] == 0:
            cnt += 1
            bfs(index)

    print(cnt)