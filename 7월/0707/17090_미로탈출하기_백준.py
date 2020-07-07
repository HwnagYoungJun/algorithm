dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def command(r, c):
    cmd = miro[r][c]
    w = None
    if cmd == 'U':
        w = 0
    elif cmd == 'R':
        w = 1
    elif cmd == 'D':
        w = 2
    elif cmd == 'L':
        w = 3
    
    nr = r + dr[w]
    nc = c + dc[w]

    return (nr, nc)


def bfs(r, c):
    foot_step = dict()
    foot_step[(r, c)] = True
    khan = 1

    while True:
        nr, nc = command(r, c)
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            for fr, fc in foot_step:
                already_escape[fr][fc] = 'True'
            return khan
        
        chk = already_escape[nr][nc]

        if chk == 'True':
            for fr, fc in foot_step:
                already_escape[fr][fc] = 'True'
            return khan
            
        elif chk == 'False':
            break

        if foot_step.get((nr, nc)) != None:
            break

        r, c = nr, nc
        khan += 1
        foot_step[(nr, nc)] = True

    for fr, fc in foot_step:
        already_escape[fr][fc] = 'False'

    return 0


N, M = map(int, input().split())
miro = [list(input()) for _ in range(N)]

escape_cnt = 0
already_escape = [[0 for _ in range(M)] for _ in range(N)]
for row in range(N):
    for col in range(M):
        if already_escape[row][col] != 0:
            continue

        res = bfs(row, col)
        escape_cnt += res

print(escape_cnt)