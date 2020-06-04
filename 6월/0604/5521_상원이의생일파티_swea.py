import sys
sys.stdin = open('5521.txt')
import collections

def bfs():
    deq = collections.deque()
    deq.append((1, 0))
    visit = {i: False for i in range(1, N + 1)}
    visit[1] = True
    invitation = 0
    while deq:
        friend, line = deq.popleft()
        for his_friend in real_friend[friend]:
            if visit[his_friend]:
                continue
            visit[his_friend] = True
            invitation += 1
            if line + 1 >= 2:
                continue
            deq.append((his_friend, line + 1))
    return invitation

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    real_friend = {i: [] for i in range(1, N + 1)}
    for _ in range(M):
        a, b = map(int, input().split())
        real_friend[a].append(b)
        real_friend[b].append(a)
    result = bfs()
    print("#{} {}".format(test_case, result))