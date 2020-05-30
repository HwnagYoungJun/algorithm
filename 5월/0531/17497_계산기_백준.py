# 1. 노가다 문제
# 2. 탐색문제가 아니다.
# <궁금한 점>
# 1. 진짜 탐색으로는 못풀까?

import sys
sys.stdin = open('17497.txt')
import collections

N = int(input())
calc = ('[+]', '[-]', '[*]', '[/]')

start = N
temp = collections.deque()
if start % 2:
    start *= 2
    temp.appendleft(['[/]'])
    
while True:
    if start < 0 or start > 2 ** 64 - 1:
        continue
    if start == 2:
        temp.appendleft('[+]')
        break
    if (start // 2) % 2 == 1:
        start -= 2
        temp.appendleft('[+]')
    else:
        start //= 2
        temp.appendleft('[*]')
    
print(len(temp))
print(*temp)
