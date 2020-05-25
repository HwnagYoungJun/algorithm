import collections

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    temp_list = list(map(int, input().split()))
    deq = collections.deque()
    for i in range(N):
        deq.append(temp_list[i])
    
    for i in range(M):
        pp = deq.popleft()
        deq.append(pp)

    print("#{} {}".format(test_case, deq[0]))
