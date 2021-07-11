import sys
import collections
sys.stdin = open('test.txt')


    # if row < 0:
    #     nr = (nr % N) + N
    # if row <= N:
    #     nr %= N

N, M, K = map(int, input().split())
fireball_info = [list(map(int, input().split())) for _ in range(M)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

map_list = [[[] for _ in range(N)] for _ in range(N)]
fireball_queue = collections.deque()
over_lap_dictionary = dict()

for i in range(M):
    fireball_info[i][0] -= 1
    fireball_info[i][1] -= 1
    fireball_queue.append(fireball_info[i])

for turn in range(1, K + 1):
    print(f'turn : {turn}')

    # 파이어볼 이동
    for _ in range(len(fireball_queue)):
        row, col, mass, speed, direction = fireball_queue.popleft()
        nr = row + (speed * dr[direction])
        nc = col + (speed * dc[direction])
        # 넘어감 처리
        if nr < 0:
            nr = (nr % N) + N
        if nr >= N:
            nr %= N
        if nc < 0:
            nc = (nc % N) + N
        if nc >= N:
            nc %= N
        
        # 딕셔너리에 임시저장
        if over_lap_dictionary.get((row, col)) == None:
            over_lap_dictionary[(row, col)] = [(nr, nc, mass, speed, direction)]
        else:
            over_lap_dictionary.append((nr, nc, mass, speed, direction))
        
    # 중첩처리
    for value in over_lap_dictionary.values():
        if len(value) > 1:
            over_lap_mass = 0
            over_lap_speed = 0
            over_lap_direction = []
            for over_lap_fireball in value:
                over_lap_mass += over_lap_fireball[2]
                over_lap_speed += over_lap_fireball[3]



        





