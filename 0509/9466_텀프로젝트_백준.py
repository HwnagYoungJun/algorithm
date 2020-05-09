import sys
sys.stdin = open('9466.txt')
sys.setrecursionlimit(150000)
input = sys.stdin.readline

# 배운점 : 재귀깊이를 늘리면 메모리초과가 날 수 있다.
#         DFS를 쓸꺼라면 재귀 제한은 미리 해제해두자.
def dfs(parent, s):
    global already_team
    global not_team
    global team

    if parent == s and s in team:
        for i in team:
            already_team[i] = 1
        not_team -= len(team)
        return

    if classroom[s] not in team and already_team[classroom[s]] == 0:
        team.add(classroom[s])
        dfs(parent, classroom[s])

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    classroom = ['X'] + list(map(int, input().split()))
    
    already_team = [0 for _ in range(N + 1)]
    not_team = N
    for student in range(1, N + 1):
        if already_team[student] == 0:
            team = set()
            dfs(student, student)
        
    print(not_team)