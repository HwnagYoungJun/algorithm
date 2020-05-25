import sys
sys.stdin = open('스타트링크.txt')
import collections

def bfs(now_floor, cnt):
    deq = collections.deque()
    deq.append((now_floor, cnt))
    visit[now_floor] = True
    delta_floor = [U, -D]

    while deq:

        floor, click = deq.popleft()
        for w in range(2):

            next_floor = floor + delta_floor[w]

            if 1 <= next_floor <= F:

                if visit[next_floor] == False:
                    
                    if next_floor == G:
                        return click + 1
                    else:
                        visit[next_floor] = True
                        deq.append((next_floor, click + 1))
    
    return 'use the stairs'


# F : 총 층수, S : 지금 있는곳, G : 목적지, U : 위로 D : 밑으로
F, S, G, U, D = map(int, input().split())
visit = [False for i in range(F + U + 1)]
count = 0

if S == G:
    print(0)

elif S < G:
    if U == 0:
        print("use the stairs")

    else:
        print(bfs(S, count))

elif S > G:
    if D == 0:
        print("use the stairs")
    else:

        print(bfs(S, count))


