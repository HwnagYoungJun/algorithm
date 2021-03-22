import sys
sys.stdin = open('11585.txt')

def make_table(keyword, table):
    i = 1
    leng = 0
    # table[0]는 무적권 0이므로 할필요가 없다
    while i < len(keyword):

        if keyword[i] == keyword[leng]:
            leng += 1
            table[i] = leng
            i += 1
        else:
            if leng:
                leng = table[leng - 1]
            else:
                table[i] = 0
                i += 1

def kmp(keyword, reference, table):
    cnt = 0
    k = 0
    r = 0
    len_k = len(keyword)
    len_r = len(reference)

    while r < len_r:

        if keyword[k] == reference[r]:
            r += 1
            k += 1
            if k == len_k:
                k = table[k - 1]
                cnt += 1
        else:
            if k:
                k = pattern[k - 1]
            else:
                r += 1
    return cnt

def hoje(a, b):
    while a > 0:
        b, a = a, b % a
    return b
N = int(input())

keyword = list(input().split())
reference = list(input().split())
reference *= 2
reference.pop()

pattern = [0 for _ in range(N)]
# 1. 테이블을 제작한다.

make_table(keyword, pattern)
a = kmp(keyword, reference, pattern)

div = hoje(a, N)

print('{}/{}'.format(a // div, N // div))