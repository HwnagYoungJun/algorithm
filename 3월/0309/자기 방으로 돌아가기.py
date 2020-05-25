import sys
sys.stdin = open('자기 방으로 돌아가기.txt')

def room(start, end):
    for i in range(start//2, end//2 + 1):
        data[i] += 1

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [0] * (200+1)
    for _ in range(N):
        start, end = map(int, input().split())
        room(min(start, end)-1, max(start, end)-1)
    print("#{0} {1}".format(tc, max(data)))
            