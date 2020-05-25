import sys
sys.stdin = open('2568.txt')
import heapq
import collections

def lis(arr):
    C = [float('inf') for _ in range(N + 1)]
    D = [0 for _ in range(N)]
    C[0] = float('-inf')
    C[1] = arr[0]
    longest = 1

    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi
        
        mid = (hi + lo) // 2
        if C[mid] == n:
            return mid
        elif n < C[mid]:
            return search(lo, mid, n)
        else:
            return search(mid + 1, hi, n)
    cnt = 0
    for n in arr:
        if C[longest] < n:
            longest += 1
            C[longest] = n
            D[cnt] = longest
        else:
            next_loc = search(0, longest, n)
            C[next_loc] = n
            D[cnt] = next_loc
        
        cnt += 1

    return longest, D

N = int(input())

temp = []
for _ in range(N) :
    a, b = map(int, input().split())
    temp.append((a, b))

temp.sort()
e = []
for i in range(N):
    e.append(temp[i][1])

no_cut, connect = lis(e)
print(N - no_cut)

f = collections.deque()
for i in range(N - 1, -1, -1):
    if no_cut == connect[i]:
        no_cut -= 1
    else:
        f.appendleft(i)

for i in f:
    print(temp[i][0])