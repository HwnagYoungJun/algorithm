import sys
sys.stdin = open('빙산.txt')
import collections
import copy

행탐색 = [0, 0, -1, 1]
열탐색 = [-1, 1, 0, 0]

def 같은빙산(r, c):
    global 빙산

    빙산덱 = collections.deque()
    빙산덱.append((r, c))
    방문확인리스트 = [[0 for _ in range(M)] for _ in range(N)]
    빙산[r][c] = 0
    방문확인리스트[r][c] = 1

    while 빙산덱:
        빙산행, 빙산열 = 빙산덱.popleft()

        for w in range(4):
            새로운행 = 빙산행 + 행탐색[w]
            새로운열 = 빙산열 + 열탐색[w]
            if 0 <= 새로운행 < N and 0 <= 새로운열 < M:
                if 방문확인리스트[새로운행][새로운열] == 0 and 빙산[새로운행][새로운열] != 0:
                    방문확인리스트[새로운행][새로운열] = 1
                    빙산[새로운행][새로운열] = 0
                    빙산덱.append((새로운행, 새로운열))


def 넓이우선탐색():
    global 빙산
    for 행 in range(N):
        for 열 in range(M):

            if 빙산[행][열] != 0:
                덱.append((행, 열, 0))

    저장시간 = -1
    저장빙산 = copy.deepcopy(빙산)

    while 덱:
        덱의행, 덱의열, 덱의시간 = 덱.popleft()
        빙산의갯수 = 0
        # print(덱의행, 덱의열, 덱의시간)

        if 저장시간 != 덱의시간:

            빙산 = copy.deepcopy(저장빙산)

            for row in range(N):
                for col in range(M):
                    
                    if 빙산[row][col] != 0:
                        # print('여기다!')
                        if 빙산의갯수 >= 1:
                            return 덱의시간
                        else:
                            빙산의갯수 += 1
                            같은빙산(row, col)
            
            빙산 = copy.deepcopy(저장빙산)

        for 방향 in range(4):
            # print('방향', 방향)
            # print(저장빙산[덱의행][덱의열])
            if 저장빙산[덱의행][덱의열] == 0:
                break
            else:
                다음행 = 덱의행 + 행탐색[방향]
                다음열 = 덱의열 + 열탐색[방향]
                # print(다음행, 다음열)
                if 0 <= 다음행 < N and 0 <= 다음열 < M:
                    if 빙산[다음행][다음열] == 0:
                        # print('?')
                        저장빙산[덱의행][덱의열] -= 1
        
        if 저장빙산[덱의행][덱의열] != 0:
            덱.append((덱의행, 덱의열, 덱의시간 + 1))

        저장시간 = 덱의시간

    return 0

N, M = map(int ,input().split())

빙산 = [list(map(int ,input().split())) for _ in range(N)]

덱 = collections.deque()

print(넓이우선탐색())



                    