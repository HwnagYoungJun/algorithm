import sys
sys.stdin = open('네트워크.txt')

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    answer = 0
    len_c = len(computers)
    visited = {row: False for row in range(len_c)}
    for row in range(len_c):
        if visited[row]:
            continue
        visited[row] = True
        answer += 1
        dfs(row, len_c, computers, visited)
    
    return answer
    
def dfs(r, len_c, computers, visited):
    for col in range(len_c):
        if visited[col]:
            continue
        if not computers[r][col]:
            continue
        visited[col] = True
        dfs(col, len_c, computers, visited)
    
print(solution(n, computers))