# 1. 11053_가장긴증가하는부분수열과 코드가 동일함
# <TIL>
# 1. 시간복잡도가 O(NlogN)으로 만들 수 있는 LIS 코드를 알게되었다.
# 2. 이진탐색의 멋짐
# <궁금한 점>
# 1. 증가하는 길이 뿐만 아니라 수열도 추적 할 수 있지 않을까?

def lis(arr):
    C = [float('inf') for _ in range(A + 1)]
    C[0] = float('-inf')
    C[1] = arr[0]
    tmp_longest = 1

    # 이진 탐색
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

    for n in arr:
        if C[tmp_longest] < n:
            tmp_longest += 1
            C[tmp_longest] = n
        else:
            next_loc = search(0, tmp_longest, n)
            C[next_loc] = n

    return tmp_longest

A = int(input())
A_list = list(map(int, input().split()))
print(lis(A_list))