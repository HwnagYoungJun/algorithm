import sys
sys.stdin = open('최솟값으로 이동하기.txt')

T = int(input())
for test_case in range(1, T + 1):
    W, H, N = map(int, input().split())
    point = list()
    for _ in range(N):
        x1, y1 = map(int, input().split())
        point.append([H - y1 , x1 - 1])
    count = 0
    for i in range(N - 1):
        r1 = point[i][0]
        c1 = point[i][1]
        r2 = point[i + 1][0]
        c2 = point[i + 1][1]
        if r1 - r2 < 0 and c1 - c2 > 0: # 좌하
            temp = min(r2 - r1, c1 - c2)
            count += temp
            count += (r2 - r1 - temp + c1 - c2 - temp)
        elif r1 - r2 > 0 and c1 - c2 < 0: # 우상
            temp = min(r1 - r2, c2 - c1)
            count += temp
            count += (r1 - r2 - temp + c2 - c1 - temp)
        else: # 이외         
            count += abs(r1 - r2) + abs(c1 - c2)
    print("#{} {}".format(test_case, count))
