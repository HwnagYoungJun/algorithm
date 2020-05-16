# 1. 투 포인터 학습을 위한 문제
# 2-1. 0~N 까지의 합이 들어있는 리스트를 생성
# 2-1-1 아니면 이때까지의 합을 저장해두는 변수를 만든다
# 2-2. 투포인터 알고리즘 실행
# 3. 크게 어려운 알고리즘은 아니지만 합문제에서 시간복잡도를 O(N)으로 끌어내리는 효율좋은 알고리즘
# <TIL>
# 1. 투 포인터!!
# <궁금한점>
# 1. 슬라이싱 윈도우 알고리즘

import sys
sys.stdin = open('2003.txt')

N, M = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 0 
S = 0 # 합 변수
count = 0

while True:
    if S >= M:
        S -= A[left]
        left += 1
    else:
        if right == N:
            break
        S += A[right]
        right += 1
    # 위 과정이 끝난 후 count를 집계
    if S == M:
        count += 1

print(count)