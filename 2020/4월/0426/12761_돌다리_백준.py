import sys
sys.stdin = open('12761.txt')
import collections


def bfs():
    deq = collections.deque()
    deq.append((N, 0))
    visit = [0 for _ in range(100000 + 1)]
    visit[N] = 1

    while deq:
        stone, cnt = deq.popleft()
        for w in range(6):
            next_stone = stone + dx[w]
            if 0 <= next_stone < 100001:
                if visit[next_stone] == 0:
                    if next_stone == M:
                        return cnt + 1
                    else:
                        visit[next_stone] = 1
                        deq.append((next_stone, cnt + 1))
        for w in [A, B]:
            next_stone = stone * w
            if 0 <= next_stone < 100001:
                if next_stone == M:
                    return cnt + 1
                else:
                    if 0 <= next_stone < 100001:
                        if visit[next_stone] == 0:
                            visit[next_stone] = 1
                            deq.append((stone * w, cnt + 1))


            

A, B, N, M = map(int, input().split())
dx = [-1, 1, -A, A, -B, B]
print(bfs())