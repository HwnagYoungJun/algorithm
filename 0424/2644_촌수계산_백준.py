import sys
sys.stdin = open('2644.txt')
import collections

def bfs():
    deq = collections.deque()
    deq.append((num1, 0))
    visit = [0 for _ in range(1 + n)]
    visit[num1] = 1
    while deq:
        go, s = deq.popleft()
        for i in chon[go]:
            if i == num2:
                return s + 1
            if visit[i] == 0:
                visit[i] = 1
                deq.append((i, s + 1))
    return -1
n = int(input())
num1, num2 = map(int, input().split())
m = int(input())

chon = [[] for _ in range(n + 1)]

for _ in range(m):
    chin1, chin2 = map(int, input().split())
    chon[chin1].append(chin2)
    chon[chin2].append(chin1)

print(bfs())
    