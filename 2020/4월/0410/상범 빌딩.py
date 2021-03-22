import sys
sys.stdin = open('상범 빌딩.txt')

# L : 높이, R : row, C : col
while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break

    # 3차원을 떠올려서 빌딩 리스트 제작
    상범빌딩 = list()

    for 아이 in range(L):
        층 = [list(input()) for 제이 in range(R)]
        상범빌딩.append(층)
        print(상범빌딩)
        

    print(상범빌딩)