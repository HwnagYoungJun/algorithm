import sys
sys.stdin = open('subtree.txt')
import collections

def bfs():
    deq = collections.deque()
    deq.append(N)
    count = 1
    while deq:
        mather= deq.popleft()
        
        for son in range(len(go_to[mather])):
            deq.append(go_to[mather][son])
            count += 1
    return count

T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    # E : 갯수, N : 루트

    temp = list(map(int ,input().split()))

    go_to = [[] for _ in range(E + 2)]

    for i in range(0, len(temp), 2):
        a = temp[i]
        b = temp[i + 1]
        go_to[a].append(b)

    result = bfs()
    print('#{} {}'.format(test_case, result))