import sys
sys.stdin = open('9205.txt')
import collections

def distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def bfs():
    deq = collections.deque()
    deq.append(house)
    visit = [0 for _ in range(N)]
    
    while deq:
        witch = deq.popleft()

        if distance(witch, festival) <= 1000:
            return 'happy'

        for w in range(N):
            if visit[w] == 0:
                if distance(witch, combi[w]) <= 1000:
                    visit[w] = 1
                    deq.append(combi[w])
    
    return 'sad'
                 

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 1000m 이상은 상근이는 갈 수 없다.

    house = list(map(int, input().split()))
    combi = [list(map(int, input().split())) for _ in range(N)]
    festival = list(map(int, input().split()))

    print(bfs())