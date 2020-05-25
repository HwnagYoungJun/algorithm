import sys
sys.stdin = open('토마토.txt')


N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]
print(a)