import sys
sys.stdin = open('13458.txt')

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

captain = 0
support = 0
for i in A:
    # 대장시험관
    i -= B
    captain += 1
    # 부대장시험관
    if i > 0:
        support += i // C
        i %= C
        if i > 0:
            support += 1

print(captain + support)
