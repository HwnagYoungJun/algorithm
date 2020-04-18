import sys
sys.stdin = open('최소 환승 경로.txt')
import collections

def bfs():

    while len(deq) != 0:
        line, lenght= deq.popleft()

        for i in range(N + 1):
            if subway[i][line] == 1:
                if i == end:
                    return lenght
                for j in range(L):
                    if j != line and subway[i][j] == 1:
                        deq.append((j, lenght + 1))

    return -1


N, L = map(int, input().split())
subway = [[0 for _ in range(L)] for _ in range(N + 1)]
for i in range(L):
    temp_list = list(map(int, input().split()))
    for j in range(len(temp_list) - 1):
        subway[temp_list[j]][i] = 1

start, end = map(int, input().split())

deq = collections.deque()

for i in range(L):
    if subway[start][i] == 1:
        deq.append((start, i, 0))
print(bfs())