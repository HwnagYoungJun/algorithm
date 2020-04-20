import sys
sys.stdin = open('6593.txt')
input = sys.stdin.readline

def se ():
    global visit
    global buliding

    start = (-1, -1, -1)
    end = (-1, -1, -1)
    
    for l in range(L):
        for r in range(R):
            for c in range(C):
                if buliding[l][r][c] == ".":
                    visit.add((l, r, c))
                elif buliding[l][r][c] == 'S':
                    start = (l, r, c)
                    buliding[l][r][c] = '.'
                    visit.add((l, r, c))
                elif buliding[l][r][c] == 'E':
                    end = (l, r, c)
                    buliding[l][r][c] = '.'
                    visit.add((l, r, c))

    return start, end


def dijkstra():
    global visit
    sl, sr, sc = start
    el, er, ec = end
    dijk = [[[float('inf') for _ in range(C)] for _ in range(R)] for _ in range(L)]
    dijk[sl][sr][sc] = 0
    row = sr
    col = sc
    height = sl
    while True:

        for w in range(6):
            nr = row + dr[w]
            nc = col + dc[w]
            nl = height + dl[w]

            if 0 <= nr < R and 0 <= nc < C and 0 <= nl < L:
                if buliding[nl][nr][nc] == '.':
                    if dijk[height][row][col] + 1 < dijk[nl][nr][nc]:
                        dijk[nl][nr][nc] = dijk[height][row][col] + 1

        visit.remove((height, row, col))
        buliding[height][row][col] == '#'
        min_dis = float('inf')

        for i in visit:
            l, r, c = i
            if min_dis > dijk[l][r][c]:
                min_dis = dijk[l][r][c]
                row = r
                col = c
                height = l
        
        if min_dis == float('inf'):
            break

    return dijk[el][er][ec]


dr = [0, 0, -1, 1, 0, 0]
dc = [-1, 1, 0, 0, 0, 0]
dl = [0, 0, 0, 0, -1, 1]

while True:
    L, R, C = map(int, input().split())

    if (L, R, C) == (0, 0, 0):
        break
    buliding = []
    for l in range(L):
        buliding.append([list(map(str, input())) for _ in range(R)])
        a= input()

    visit = set()
    start, end = se()
    result = dijkstra()
    
    if result == float('inf'):
        result = "Trapped!"
        print(result)
    else:
        print("Escaped in {} minute(s)".format(result))