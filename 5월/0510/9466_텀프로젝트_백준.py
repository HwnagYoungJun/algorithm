import sys
sys.stdin = open('9466.txt')
sys.setrecursionlimit(111111)
input = sys.stdin.readline

# 배운점 : 재귀깊이를 늘리면 메모리초과가 날 수 있다.
#         DFS를 쓸꺼라면 재귀 제한은 미리 해제해두자.
def dfs(s):
    global team
    global already_team
    global no_friend

    already_team[s] = 1
    team.append(s)

    next_student = classroom[s]
    if already_team[next_student] == 1:
        if next_student in team:
            no_friend -= len(team[team.index(next_student):])
            return
    else:
        dfs(next_student)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    classroom = ['X'] + list(map(int, input().split()))
    
    already_team = [0 for _ in range(N + 1)]
    already_team[0] = float('inf')

    no_friend = N
    for student in range(1, N + 1):
        if already_team[student] == 0:
            team = list()
            dfs(student)
    print(no_friend)