import collections

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 1의 번호를 가진 어른 상어는 강력해서 다 쫓아 낼 수 있다.
N, M, k = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(N)]

init_direction = list(map(int, input().split()))

# queue를 사용, 상어를 관리
# 냄새는 2차원 배열로 관리
deq = collections.deque()

smell =  [[0 for _ in range(N)] for _ in range(N)]
sd = 0
for row in range(N):
    for col in range(N):
        if map_list[row][col] != 0:
            deq.append((map_list[row][col], row, col, init_direction[map_list[row][col] - 1]))
            map_list[row][col] = 0

command = dict()
for i in range(1, M + 1):
    command[i] = [list(map(int, input().split())) for _ in range(4)]
time = 0
# 1000 초가 넘으면 안된다.
while time <= 1000:
    time += 1
    # 시간 별로 움직여보자
    # 냄새관리를 하자
    for r in range(N):
        for c in range(N):
            if smell[r][c] != 0:
                if smell[r][c][1] == 1:
                    smell[r][c] = 0
                else:
                    smell[r][c][1] -= 1
    
    for i in deq:
        smell[i[1]][i[2]] = [i[0], k]


    # for j in smell:
    #     print(*j)
    # print()
    # print(deq)
    # 상어의 이동
    for _ in range(len(deq)):
        shark_num, row, col, d = deq.popleft()
        possible_d = []

        # 4방향에 냄새가 있는지 체크
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if smell[nr][nc] == 0:
                    possible_d.append(w + 1)
        # 4방향에 내 냄새가 있는지 체크
        if possible_d == []:
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < N and 0 <= nc < N:
                    if smell[nr][nc] != 0:
                        if smell[nr][nc][0] == shark_num:
                            possible_d.append(w + 1)

        if possible_d:
            # print(shark_num, possible_d, d)
            # print(command[shark_num][d-1])
            for c in command[shark_num][d - 1]:
                # print(c)
                if c in possible_d:
                    nr = row + dr[c - 1]
                    nc = col + dc[c - 1]
                    # 그곳에 상어가 있다면
                    if map_list[nr][nc] != 0:
                        if map_list[nr][nc][0] < shark_num:
                            pass
                        else:
                            deq.remove((map_list[nr][nc][0], nr, nc, map_list[nr][nc][1]))
                            map_list[nr][nc] = [shark_num, c]
                            deq.append((shark_num, nr, nc, c))
                    # 없다면
                    else:
                        deq.append((shark_num, nr, nc, c))
                        map_list[nr][nc] = [shark_num, c]
                    # 움직였으니 그곳을 0으로 만들고 대탈출    
                    break
    
    # for i in map_list:
    #     print(*i)
    # print()
    if len(deq) == 1:
        break
    map_list = [[0 for _ in range(N)] for _ in range(N)]
if time == 1001:
    print(-1)
else:
    print(time)