import sys
sys.stdin = open('피자굽기.txt')
import collections

def bfs():
    for i in range(1, N + 1):
        deq.append((i, pizza[i - 1]))
    p = N + 1
    while len(deq) != 1:
        pizza_num, bcheeze = deq.popleft()
        cheeze = bcheeze // 2

        if cheeze == 0:
            if p <= M:
                deq.append((p, pizza[p - 1]))
                p += 1
        else:
            deq.append((pizza_num, cheeze))
    return deq[0][0]

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    deq = collections.deque()
    result = bfs()

    print("#{} {}".format(test_case, result))

