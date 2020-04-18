import sys
sys.stdin = open("나무 재테크.txt")


dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

N, M, K = map(int ,input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# 포레스트 리스트의 0: 양분, 1: 나무들의 나이의 리스트, 2: 죽기시작하는 인덱스 안죽으면 "NO"로 남아있겠지
forest = [[[5,[], 'NO'] for _ in range(N)] for _ in range(N)]

amount_tree = 0

for i in range(M):
    r, c, age = map(int, input().split())
    r -= 1
    c -= 1
    forest[r][c][1].append(age)

for i in range(K):
    # 봄에는 양분을 먹는다.
    for row in range(N):
        for col in range(N):
            forest[row][col][1].sort()
            forest[row][col][2] = 'NO'
            for x in range(len(forest[row][col][1])):
                if forest[row][col][1][x] <= forest[row][col][0]:
                    forest[row][col][0] -= forest[row][col][1][x]
                    forest[row][col][1][x] += 1
                else:
                    forest[row][col][2] = x
                    break
            
            if forest[row][col][2] != 'NO':
                for y in range(forest[row][col][2], len(forest[row][col][1])):
                    forest[row][col][0] += forest[row][col][1][y] // 2
                forest[row][col][1] = forest[row][col][1][:forest[row][col][2]]
    # 여름에는 죽은 나무가 나이 // 2 만큼 나이를 먹는다.
    # 따로 해주면 왠지 시간초과가 날 것같아서 봄에 같이 할 방법을 찾아본다.

    # 가을에는 팔방향 나무를 심어준다 같이 못할꺼같아서 다시 한번더 탐색
    # 겨울은 가을에 담아준다

    for row in range(N):
        for col in range(N):
            forest[row][col][0] += A[row][col]
            for z in range(len(forest[row][col][1])):
                if forest[row][col][1][z] % 5 == 0:
                    for w in range(8):
                        nr = row + dr[w]
                        nc = col + dc[w]
                        if 0 <= nr < N and 0 <= nc < N:
                            forest[nr][nc][1].append(1)

    # 숫자세는걸 어떻게 탐색할때 한방에 할지를 몰라서 따로 했다.
    if i == K - 1:
        for row in range(N):
            for col in range(N):
                amount_tree += len(forest[row][col][1])
    
print(amount_tree)

                
        
