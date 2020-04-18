import sys
sys.stdin = open('드래곤 커브.txt')
N = int(input())
x, y, d, g = map(int, input().split())
dragon = [[0 for _ in range(100)] for _ in range(100)]
d 