import sys
sys.stdin = open('역사.txt')
import collections


def bfs(start, end):
    deq = collections.deque()
    deq.append(start)
    visit = [0] * (n + 1)
    visit[start] = 1
    while deq:
        go = deq.popleft()

        for destination in save[start]:
            if visit[destination] == 0 and history[go][destination] == 1:
                if destination == end:
                    return -1
                else:
                    visit[destination] = 1
                    deq.append(destination)


    deq.clear()  # 없는걸 알지만 불안한 마음에 그냥 한번 적어봤어
    deq.append(end)
    visit = [0] * (n + 1)
    visit[end] = 1
    while deq:
        go = deq.popleft()

        for destination in save[end]:
            if visit[destination] == 0 and history[go][destination] == 1:
                if destination == start:
                    return 1
                else:
                    visit[destination] = 1
                    deq.append(destination)
    return 0


n, k = map(int, input().split())
history = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
save = [[] for _ in range(n + 1)]
for i in range(k):
    s1, s2 = map(int, input().split())
    save[s1].append(s2)
    history[s1][s2] = 1


s = int(input())
for j in range(s):
    a, b = map(int, input().split())

    print(bfs(a, b))
    