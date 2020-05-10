import sys
sys.stdin = open('2564.txt')

C, R = map(int, input().split())

N = int(input())

point = [list(map(int, input().split())) for _ in range(N + 1)]
guard = point.pop()

result = 0
gd, gw = guard

if gd == 1:
    for d, w in point:
        if d == 1:
            result += abs(gw - w)
        elif d == 2:
            result += (R + min(gw + w, 2 * C - gw - w))
        elif d == 3:
            result += gw + w
        elif d == 4:
            result += (C - gw) + w

elif gd == 2:
    for d, w in point:
        if d == 1:
            result += (R + min(gw + w, 2 * C - gw - w))
        elif d == 2:
            result += abs(gw - w)
        elif d == 3:
            result += gw + (R - w)
        elif d == 4:
            result += (R - gw) + (C - w)

elif gd == 3:
    for d, w in point:
        if d == 1:
            result += gw + w
        elif d == 2:
            result += (R - gw) + w
        elif d == 3:
            result += abs(gw - w)
        elif d == 4:
            result += (C + min(gw + w, 2 * R - gw - w))

elif gd == 4:
    for d, w in point:
        if d == 1:
            result += gw + (R - w)
        elif d == 2:
            result += (C - gw) + (R - w)
        elif d == 3:
            result += (C + min(gw + w, 2 * R - gw -w))
        elif d == 4:
            result += abs(gw - w)

print(result)