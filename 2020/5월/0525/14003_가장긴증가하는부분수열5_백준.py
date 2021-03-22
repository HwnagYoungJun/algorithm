import sys
sys.stdin = open('14003.txt')
input = sys.stdin.readline

def lis(arr):
    C = [float('inf') for _ in range(A + 1)]
    D = [0 for _ in range(A)]
    C[0] = float('-inf')
    C[1] = arr[0]
    longest = 1

    def search(lo, hi, n):
        if lo == hi:
            return lo
        elif lo + 1 == hi:
            return lo if C[lo] >= n else hi

        mid = (lo + hi) // 2
        if C[mid] == n:
            return mid
        elif C[mid] > n:
            return search(lo, mid, n)
        else:
            return search(mid + 1, hi, n)
    
    cnt = 0
    for n in arr:
        if C[longest] < n:
            longest += 1
            C[longest] = n
            D[cnt] = longest - 1
        else:
            next_loc = search(0, longest, n)
            C[next_loc] = n
            D[cnt] = next_loc - 1
        cnt += 1
    
    return longest, D

A = int(input())
A_list = list(map(int, input().split()))

cnt, E = lis(A_list)
print(cnt)
cnt -= 1
F = []
for i in range(A):
    if cnt == E.pop():
        F.append(A_list[A - 1 - i])
        cnt -= 1
print(*(reversed(F)))