drc = [[(1, 0), (2, 0), (3, 0)], [(0, 1), (0, 2), (0, 3)], [(1, 1), (1, 0), (0, 1)], [(1, 2), (0, 2), (0, 1)], [(-1, 2), (0, 2), (0, 1)], [(-1, 0), (0, 2), (0, 1)], [(0, 2), (0, 1), (1, 0)], [(2, 1), (1, 1), (0, 1)], [(-2, 1), (-1, 1), (0, 1)], [(2, -1), (1, -1), (0, -1)], [(-2, -1), (-1, -1), (0, -1)], [(1, 2), (1, 1), (0, 1)], [(-1, 2), (-1, 1), (0, 1)], [(2, 1), (1, 1), (1, 0)], [(-2, 1), (-1, 1), (-1 , 0)], [(1, 1), (2, 0), (1, 0)], [(1, -1), (2, 0), (1, 0)], [(0, 2), (0, 1), (1, 1)], [(0, 2), (0, 1), (-1, 1)]]

def tetro(row, col):
  max_value = float('-inf')
  reset_value = map_list[row][col]
  for d in drc:
    this_value = reset_value

    for w in range(3):
      nr = row + d[w][0]
      nc = col + d[w][1]

      if nr < 0 or nr >= N or nr < 0 or nc >= M:
        break

      this_value += map_list[nr][nc]

    max_value = max(max_value, this_value)

  return max_value
        
N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
result = float('-inf')

for row in range(N):
  for col in range(M):
    result = max(result, tetro(row, col))
  
print(result)