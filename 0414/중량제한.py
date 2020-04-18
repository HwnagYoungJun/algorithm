import sys
sys.stdin = open('중량제한.txt')

import collections

def bfs():
    global result

    deq = collections.deque()
    deq.append((start_factory, float('inf'), {start_factory}))

    while deq:
        go, amount, foot_step = deq.popleft()
        print(go, amount)
        for next_is, am in go_to[go].items():
            if next_is not in foot_step:
                if next_is == end_factory:
                    if min(amount, am) > result:
                        result = min(amount, am)
                else:
                    deq.append((next_is, min(amount, am), foot_step | {next_is}))

N, M = map(int, input().split())

go_to = [{} for _ in range(N + 1)]
for i in range(M):
    s1, s2, middle_amount = map(int, input().split())
    if s2 not in go_to[s1]:
        go_to[s1][s2] = middle_amount
    else:
        if middle_amount > go_to[s1][s2]:
            go_to[s1][s2] = middle_amount
    if s1 not in go_to[s2]:
        go_to[s2][s1] = middle_amount
    else:
        if middle_amount > go_to[s2][s1]:
            go_to[s2][s1] = middle_amount

start_factory, end_factory = map(int, input().split())
result = float('-inf')
bfs()
print(result)