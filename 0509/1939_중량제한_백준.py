import sys
sys.stdin = open('1939.txt')
import collections
input = sys.stdin.readline

def bfs():
    global result

    deq = collections.deque()
    deq.append((start_factory, float('inf')))
    weight = [-1 for _ in range(N + 1)]
    weight[start_factory] = float('inf')

    while deq:
        go, amount = deq.popleft()

        for next_is, am in go_to[go].items():
            value = min(am, amount)
            if weight[next_is] < value:
                weight[next_is] = value
                if next_is != end_factory:
                    deq.append((next_is, value))
            
    return weight[end_factory]

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
print(bfs())