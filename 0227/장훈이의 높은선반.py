import sys
sys.stdin = open('장훈이의 높은선반.txt')
T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    # temp_list = list() # 경우의 수 담을 리스트
    result = list() # 결과 리스트
    chk = 10000 * 20 + 1 # 최대 키
    for i in range(1, 2 ** N - 1): # 경우의 수
        temp = list(format(i, 'b').zfill(N))
        count = 0
        for j in range(N):
            if temp[j] == '1':
                count += height[j]
        if count >= B and count < chk:
            chk = count
        if chk == B: # 조금이라도 시간을 줄이고 싶음
            break
    result = chk - B
    print('#{} {}'.format(test_case, result))