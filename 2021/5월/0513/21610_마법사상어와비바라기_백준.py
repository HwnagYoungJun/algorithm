dr4 = [-1, -1, 1, 1]
dc4 = [-1, 1, 1, -1]

dr8 = [None, 0, -1, -1, -1, 0, 1, 1, 1]
dc8 = [None, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(N)]
move_list = [list(map(int, input().split())) for _ in range(M)]

cloud_list = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

for step in range(M):
    pos_move = move_list[step]

    # 1. 구름의 이동 and 비 내리기
    len_clound_list = len(cloud_list)

    for i in range(len_clound_list):
        row, col = cloud_list[i]

        row += dr8[pos_move[0]] * pos_move[1]
        col += dc8[pos_move[0]] * pos_move[1]

        if row < 0 or row >= N:
            row = row % N
        if col < 0 or col >= N:
            col = col % N
        cloud_list[i] = (row, col)
        map_list[row][col] += 1

    # 2. 물복사 버그
    cloud_map = [[0 for _ in range(N)] for _ in range(N)]  # 구름이 있는곳을 체크하는 맵
    for i in range(len_clound_list):
        row, col = cloud_list[i]
        cloud_map[row][col] = 1

        for w in range(4):
            nr = row + dr4[w]
            nc = col + dc4[w]

            if (nr < 0 or nr >= N or nc < 0 or nc >= N):
                continue
            if (map_list[nr][nc] == 0):
                continue
            map_list[row][col] += 1

    # 3. 새로운 구름의 생성
    new_cloud_list = []
    for row in range(N):
        for col in range(N):

            if map_list[row][col] >= 2:
                if cloud_map[row][col] == 0:
                    map_list[row][col] -= 2
                    new_cloud_list.append((row, col))

    cloud_list = new_cloud_list[:]

result = 0
for i in range(N):
    result += sum(map_list[i])

print(result)