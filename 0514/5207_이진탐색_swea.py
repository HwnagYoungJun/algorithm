def my_search(num, count):
    global count
    start = 0
    end = len(A) - 1
    mode = 0
    while True:
        mid = A[(start + end) // 2]
        if mid == num:
            count += 1
            return
        if num > mid:
            if mode == 'right':
                return
            start = A.index(mid) + 1
            mode = 'right'
        
        elif num < mid:
            if mode == 'left':
                return
            end = A.index(mid) - 1
            mode = 'left'

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A = sorted(A)
    B = list(map(int, input().split()))
    count = 0
    for word in B:
        my_search(word, count)
    print("#{} {}".format(test_case, count))