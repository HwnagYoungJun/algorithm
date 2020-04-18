import sys
sys.stdin = open('노드의 거리.txt')
import collections
def bfs(row, k):
    visit[row] = 1
    deq.append((row, k))

    while len(deq) != 0:
        br, bk = deq.popleft()
        if br == end:
            return bk
        for col in range(1, V + 1):
            if node[br][col] == 1 and visit[col] == 0:
                visit[col] = 1
                deq.append((col, bk + 1))
    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for i in range(E):
        num1, num2 = map(int, input().split())
        node[num1][num2] = 1
        node[num2][num1] = 1
    visit = [0 for _ in range(V + 1)]
    start, end = map(int, input().split())
    deq = collections.deque()
    result = bfs(start, 0)
    print("#{} {}".format(test_case, result))