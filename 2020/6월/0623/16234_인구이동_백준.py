import sys
sys.stdin = open('16234.txt')
import collections
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(r, c, union_num):
    global total_population
    deq = collections.deque()
    deq.append((r, c))
    union[r][c] = union_num
    union_countries.append((r, c))
    total_population += country_list[r][c]
    while deq:
        row, col = deq.popleft()
        for w in range(4):
            nr = row + dr[w]
            nc = col + dc[w]
            if 0 <= nr < N and 0 <= nc < N:
                if union[nr][nc] == 0:
                    if (nr, nc) in border[(row, col)]:
                        union[nr][nc] = union_num
                        deq.append((nr, nc))
                        union_countries.append((nr, nc))
                        total_population += country_list[nr][nc]

# N X N, L명 이상 R명 이하

# 1. 국경선 맵을 만든다.
# 2. 국경선을 개방한다.
# 3. BFS로 연합을 나눈다.
# 4. 인구를 나눈다.
# 5. 반복한다.

# 예상시간복잡도 : 2000 X ((50 X 50 X 4) + (50 X 50)) = 25,000,000 -> 250ms
N, L, R = map(int, input().split())
country_list = [list(map(int, input().split())) for _ in range(N)]

count = 0
while True:
    # num1 나라랑 num2번 나라의 국경선 맵
    # (row, col) 나라는 []안에 있는 나라랑 연합을 맺었다 라는 뜻의 맵
    border = {(row, col): [] for row in range(N) for col in range(N)}
    # 2. 국경선을 개방한다.
    for row in range(N):
        for col in range(N):
            # 4방향 탐색
            for w in range(4):
                nr = row + dr[w]
                nc = col + dc[w]
                if 0 <= nr < N and 0 <= nc < N:
                    if L <= abs(country_list[row][col] - country_list[nr][nc]) <= R:
                        border[(row, col)].append((nr, nc))
    # 3. BFS로 연합을 나눈다.
    union = [[0 for _ in range(N)] for _ in range(N)]
    union_num = 1
    chk = False
    for row in range(N):
        for col in range(N):
            if union[row][col] == 0:
                union_countries = []
                total_population = 0
                bfs(row, col, union_num)
                # 4. 인구를 나눈다.
                if len(union_countries) != 1:
                    for cr, cc in union_countries:
                        country_list[cr][cc] = total_population // len(union_countries)
                union_num += 1    

    # 5. 반복한다.
    if union_num != N ** 2 + 1:
        count += 1
    else:
        break
print(count)