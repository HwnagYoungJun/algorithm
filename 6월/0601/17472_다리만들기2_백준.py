import sys
sys.stdin = open('17472.txt')
import collections

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]


def bfs(row, col, name):
    global island
    deq = collections.deque()
    deq.append((row, col))
    while deq:
        r, c = deq.popleft()
        for w in range(4):
            nr = r + dr[w]
            nc = c + dc[w]
            if 0 <= nr < N and 0 <= nc < M:
                if map_list[nr][nc] == 1:
                    map_list[nr][nc] = name
                    island[name].append((nr, nc))
                    deq.append((nr, nc))

def find_min_dist(i1):
    for row, col in island[i1]:
        # 좌
        r = row
        c = col
        d = -1
        while c > 0:
            d += 1
            c -= 1
            if map_list[r][c] == i1:
                break
            elif map_list[r][c] != 0:
                i2 = map_list[r][c]
                if d == 1:
                    break
                E_list.append((i1, i2, d))
                conject[i1].append(i2)
                conject[i2].append(i1)
                break
        # 우
        r = row
        c = col
        d = -1
        while c < M - 1:
            d += 1
            c += 1
            if map_list[r][c] == i1:
                break
            elif map_list[r][c] != 0:
                i2 = map_list[r][c]
                if d == 1:
                    break
                E_list.append((i1, i2, d))
                conject[i1].append(i2)
                conject[i2].append(i1)
                break
        # 상
        r = row
        c = col
        d = -1
        while r > 0:
            d += 1
            r -= 1
            if map_list[r][c] == i1:
                break
            elif map_list[r][c] != 0:
                i2 = map_list[r][c]
                if d == 1:
                    break
                E_list.append((i1, i2, d))
                conject[i1].append(i2)
                conject[i2].append(i1)
                break
        # 하
        r = row
        c = col
        d = -1
        while r < N - 1:
            d += 1
            r += 1
            if map_list[r][c] == i1:
                break
            elif map_list[r][c] != 0:
                i2 = map_list[r][c]
                if d == 1:
                    break
                E_list.append((i1, i2, d))
                conject[i1].append(i2)
                conject[i2].append(i1)
                break
    return
    
def connection():
    deq = collections.deque()
    deq.append(2)
    visit = {i : False for i in range(2, island_name + 1)}
    visit[2] = True
    while deq:
        this_sum = deq.popleft()
        for next_sum in conject[this_sum]:
            if visit[next_sum]:
                continue
            visit[next_sum] = True
            deq.append(next_sum)
    
    for i in range(2, island_name + 1):
        if not visit[i]:
            return False
    return True

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    fx = find(x)
    fy = find(y)
    if fx != fy:
        parent[fy] = fx

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]

island = dict()
island_name = 1
for row in range(N):
    for col in range(M):
        if map_list[row][col] == 1:
            island_name += 1
            map_list[row][col] = island_name
            island[island_name] = [(row, col)]
            bfs(row, col, island_name)

E_list = []
conject = {i : [] for i in range(2, island_name + 1)}
parent = {i : i for i in range(2, island_name + 1)}
for i1 in range(2, island_name + 1):
    find_min_dist(i1)

E_list.sort(key=lambda x: x[2])
island_connection = connection()
if island_connection:
    total_cost = 0
    for island1, island2, cost in E_list:
        if find(island1) != find(island2):
            union(island1, island2)
            total_cost += cost
    print(total_cost)
else:
    print(-1)
