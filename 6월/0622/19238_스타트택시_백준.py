import sys
sys.stdin = open('19238.txt')
import collections
# N X N 격자, M명의 승객, K: 초기연료
# 승객을 태울때에는 현 위치에서 최단거리, 만약 같다면 col이 작은 승객
# 한칸을 이동할 때마다 연료 1소모 
# 승객을 태워 이동하면 소모한 연료의 두 배 충전
# 목적지로 이동시킨 동시에 연료가 바닥나면 성공한 것으로 간주

def bfs(s, f):
    deq = collections.deque()
    deq.append(s)
    visit = {(row, col): False for row in range(N) for col in range(N)}
    visit[s] = True
    fast_passengers = []
    time = 0
    if map_list[s[0]][s[1]] > 1:
        p_num = map_list[s[0]][s[1]] - 1
        map_list[s[0]][s[1]] = 0
        return ((s[0], s[1], p_num), 0)
    while deq:
        if fast_passengers:
            real_fast = (float('inf'), float('inf'))
            for fast_passenger in fast_passengers:
                if real_fast[0] > fast_passenger[0]:
                    real_fast = fast_passenger
                elif real_fast[0] == fast_passenger[0]:
                    if real_fast[1] > fast_passenger[1]:
                        real_fast = fast_passenger
            
            map_list[real_fast[0]][real_fast[1]] = 0
            return (real_fast, time)

        for _ in range(len(deq)):
            row, col = deq.popleft()
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < N and 0 <= nc < N:
                    if not visit[(nr, nc)]:
                        if map_list[nr][nc] == 0:
                            visit[(nr, nc)] = True
                            deq.append((nr, nc))
                        elif map_list[nr][nc] > 1:
                            visit[(nr, nc)] = True
                            fast_passengers.append((nr, nc, map_list[nr][nc] - 1))
        
        time += 1
        if time >= f:
            return (-1, -1)

    if fast_passengers:
        real_fast = (float('inf'), float('inf'))
        for fast_passenger in fast_passengers:
            if real_fast[0] > fast_passenger[0]:
                real_fast = fast_passenger
            elif real_fast[0] == fast_passenger[0]:
                if real_fast[1] > fast_passenger[1]:
                    real_fast = fast_passenger

        map_list[real_fast[0]][real_fast[1]] = 0
        return (real_fast, time)
    else:
        return (-1, -1)

def destination(s, e, f):
    deq = collections.deque()
    deq.append((s[0], s[1], 0))
    visit = {(row, col): False for row in range(N) for col in range(N)}
    visit[s] = True

    while deq:
        row, col, time = deq.popleft()

        if time >= f:
            return (-1, -1)
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]    
            if 0 <= nr < N and 0 <= nc < N:
                if not visit[(nr, nc)]:
                    if map_list[nr][nc] == 1:
                        continue

                    if (nr, nc) == e:
                        return ((nr, nc), time + 1)

                    visit[(nr, nc)] = True
                    deq.append((nr, nc, time + 1))
    
    return (-1, -1)

    
dr = [-1, 1, 0, 0]
dc = [0, 0, -1 ,1]

N, M, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
s1, s2 = map(int, input().split())
start = (s1 - 1, s2 - 1)
passenger = dict()

for i in range(1, M + 1):
    a, b, c, d = map(int, input().split())
    passenger[i] = [a - 1, b - 1, c - 1, d - 1]

    map_list[a - 1][b - 1] = i + 1

for _ in range(M):
    # 짧은 승객 찾기
    # print(start, K)
    complete, t = bfs(start, K)
    if complete == -1:
        print(-1)
        break
    else:
        K -= t
        start = (complete[0], complete[1])

    # 대려다주기
    # print(complete)
    # print(start, (passenger[complete[2]][2], passenger[complete[2]][3]), K)
    complete, t = destination(start, (passenger[complete[2]][2], passenger[complete[2]][3]), K)
    if complete == -1:
        print(-1)
        break
    else:
        K += t
        start = complete
else:
    print(K)
    