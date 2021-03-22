import sys
sys.stdin = open('1707.txt')
import collections

def bfs(n):
    deq = collections.deque()
    deq.append((n, 'RED'))
    visit[n] = [True, 'RED']
    while deq:
        node, color = deq.popleft()
        for next_node in conj[node]:
            if not visit[next_node][0]:
                if color == 'RED':
                    visit[next_node] = [True, 'BLACK']
                    deq.append((next_node, 'BLACK'))
                else:
                    visit[next_node] = [True, 'RED']
                    deq.append((next_node, 'RED'))
            else:
                if color == visit[next_node][1]:
                    return 'NO'
    return 'YES'

T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    conj = {i: [] for i in range(1, V + 1)}
    for _ in range(E):
        n1, n2 = map(int, input().split())
        conj[n1].append(n2)
        conj[n2].append(n1)

    visit = {i: [False, 'NO'] for i in range(V + 1)}
    for n in range(1, V + 1):
        if not visit[n][0]:
            result = bfs(n)
            if result == 'NO':
                print(result)
                break
    else:
        print('YES')