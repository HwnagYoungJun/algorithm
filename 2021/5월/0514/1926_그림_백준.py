import collections


def bfs(row, col):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    deq = collections.deque()
    deq.append((row, col))
    draw_paper[row][col] = -1
    size = 1
    
    while len(deq) > 0:
        pos_row, pos_col = deq.popleft()
        for w in range(4):
            new_row = pos_row + dr[w]
            new_col = pos_col + dc[w]
            if 0 <= new_row < n and 0 <= new_col < m:
                if draw_paper[new_row][new_col] == 1:
                    size += 1
                    draw_paper[new_row][new_col] = -1
                    deq.append((new_row, new_col))

    return size


n, m = map(int, input().split(" "))
draw_paper = [list(map(int, input().split(" "))) for _ in range(n)]

max_size = 0
draw_count = 0

for row in range(n):
    for col in range(m):
        if draw_paper[row][col] == 1:
            draw_count += 1
            draw_size = bfs(row, col)
            if draw_size > max_size:
                max_size = draw_size

print(draw_count)
print(max_size)