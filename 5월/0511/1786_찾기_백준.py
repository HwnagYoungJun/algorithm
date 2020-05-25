import sys
sys.stdin = open('1786.txt')
input = sys.stdin.readline

def kmp_table(keyword):
    global pattern
    i = 1
    leng = 0

    while  i < len(keyword):
        if keyword[i] == keyword[leng]:
            leng += 1
            pattern[i] = leng
            i += 1
        else:
            if leng:
                leng = pattern[leng - 1]
            else:
                pattern[i] = 0
                i += 1
    
def kmp(keyword, reference):
    index = list()
    r = 0 # 레퍼런스의 인덱스
    k = 0 # 키워드의 인덱스
    len_k = len(keyword)
    len_r = len(reference)
    while r < len_r:
        if keyword[k] == reference[r]:
            r += 1
            k += 1
            if k == len_k:
                index.append(r - k + 1)
                k = pattern[k - 1]
        else:
            if k:
                k = pattern[k - 1]
            else:
                r += 1
    
    return index

# KMP 알고리즘으로 풀어볼것이다.

T = input()
blank = 0
P = input()

pattern = [0 for _ in range(len(P))]
# 1. KMP 테이블을 제작한다.

kmp_table(P)

# 2. KMP 알고리즘을 실시한다.

result = kmp(P, T)
print(len(result))
print(*result)