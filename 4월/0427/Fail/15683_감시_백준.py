import sys
sys.stdin = open('15683.txt')
import collections

# def dfs(k, alart):
#     global gamsi
#     if k == len(cctv):
#         return
#     row = cctv[k][0]
#     col = cctv[k][1]
#     case = cctv[k][2]
#     if case == 1:
#         for w in range(4):
#             case1(row, col, w)
#             dfs(k + 1)
#             clean1(row, col, w)
#     elif case == 2:
#         for w in range(2):
#             case2(row, col, w)
#             dfs(k + 1)
#             clean2(row, col, w)
#     elif case == 3:
#         for w in range(4):
#             case3(row, col, w)
#             dfs(k + 1)
#             clean3(row, col, w)
#     if case == 1:
#         for w in range(4):
#             case1(row, col, w)
#             dfs(k + 1)
#             case1(row, col, w)
#     if case == 1:
#         for w in range(4):
#             case1(row, col, w)
#             dfs(k + 1)
#             case1(row, col, w)

# def case1(r, c, n):
#     global gamsi

#     if n == 0: # 좌
#         for i in range(c, -1, -1):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 1
#             else:
#                 break
#     elif n == 1: # 우
#         for i in range(c, M):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 1
#             else:
#                 break
#     elif n == 2: # 상
#         for i in range(r, -1, -1):
#             if gamsi[r][i] != 6:  
#                 gamsi[i][c] = 1
#             else:
#                 break
#     elif n == 3: # 하  
#         for i in range(r, N):
#             if gamsi[r][i] != 6:
#                 gamsi[i][c] = 1
#             else:
#                 break
#     return

# def clean1(r, c, n):
#     global gamsi

#     if n == 0: # 좌
#         for i in range(c, -1, -1):
#             if gamsi[r][i] == 1:
#                 gamsi[r][i] = 0
#             else:
#                 break
#         gamsi[r][c] = 1
        
#     elif n == 1: # 우
#         for i in range(c, M):
#             if gamsi[r][i] == 1:
#                 gamsi[r][i] = 0
#             else:
#                 break
#         gamsi[r][c] = 1
#     elif n == 2: # 상
#         for i in range(r, -1, -1):
#             if gamsi[i][c] == 1:
#                 gamsi[i][c] = 0
#             else:
#                 break
#         gamsi[r][c] = 1
#     elif n == 3: # 하  
#         for i in range(r, N):
#             if gamsi[i][c] == 1:
#                 gamsi[i][c] = 0
#             else:
#                 break
#         gamsi[r][c] = 1
#     return

# def case2(r, c, n):
#     global gamsi
#     if n == 0:
#         for i in range(c, -1, -1):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 2
#             else:
#                 break
#         for i in range(c, M):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 2
#             else:
#                 break
#     elif n == 1:
#         for i in range(r, -1, -1):
#             if gamsi[r][i] != 6:  
#                 gamsi[i][c] = 2
#             else:
#                 break
#         for i in range(r, N):
#             if gamsi[r][i] 1= 6:
#                 gamsi[i][c] = 2
#             else:
#                 break
#     return

# def clean2(r, c, n):
#     global gamsi

#     if n == 0: 
#         for i in range(c, -1, -1):
#             if gamsi[r][i] == 2:
#                 gamsi[r][i] = 0
#             else:
#                 break
#         gamsi[r][c] = 2
#         for i in range(c, M):
#             if gamsi[r][i] == 2:
#                 gamsi[r][i] = 0
#             else:
#                 break
#         gamsi[r][c] = 2
#     elif n == 2: 
#         for i in range(r, -1, -1):
#             if gamsi[i][c] == 2:
#                 gamsi[i][c] = 0
#             else:
#                 break
#         gamsi[r][c] = 2

#         for i in range(r, N):
#             if gamsi[i][c] == 2:
#                 gamsi[i][c] = 0
#             else:
#                 break
#         gamsi[r][c] = 2
#     return

# def case3(r, c, n):
#     global gamsi

#     if n == 0: # 좌
#         for i in range(c, -1, -1):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 3
#             else:
#                 break
#         for i in range(r, -1, -1):
#             if gamsi[r][i] != 6:  
#                 gamsi[i][c] = 3
#             else:
#                 break
#     elif n == 1: # 우
#         for i in range(c, -1, -1):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 3
#             else:
#                 break
#         for i in range(r, N):
#             if gamsi[r][i] != 6:
#                 gamsi[i][c] = 3
#             else:
#                 break


#     elif n == 2:
#         for i in range(r, -1, -1):
#             if gamsi[r][i] != 6:  
#                 gamsi[i][c] = 3
#             else:
#                 break
#         for i in range(c, M):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 1
#             else:
#                 break
        
#     elif n == 3: # 하  
#         for i in range(r, N):
#             if gamsi[r][i] == 0:
#                 gamsi[i][c] = 1
#             else:
#                 break
#         for i in range(c, M):
#             if gamsi[r][i] != 6:
#                 gamsi[r][i] = 1
#             else:
#                 break
#     return

# def clean3(r, c, n):

N, M = map(int, input().split())

gamsi = [list(map(int, input().split())) for _ in range(N)]
cctv = collections.deque()
safe = 0
for row in range(N):
    for col in range(M):
        if gamsi[row][col] != 0 and gamsi[row][col] != 6:
            cctv.append((row, col, gamsi[row][col]))
        if gamsi[row][col] == 0:
            safe += 1


# dfs(0, 0)