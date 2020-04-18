import sys
sys.stdin = open("미생물 격리.txt")
import collections

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split()) # N: 크기, K: 최초군집갯수, M: 격리시간     
    deq = collections.deque()
    for i in range(K):
        r, c, num, d = map(int, input().split())
        deq.append((r, c, num, d, 0))
    count = 0
    result = 0
    sv_k = -1
    while True:

        row, col, amount, direction, k = deq.popleft()
        amount = int(amount)
        if k == M:
            result += amount
            for i in range(len(deq)):
                result += int(deq[i][2])
            break
        if k != sv_k:
            data_storage = [[0 for _ in range(N)] for _ in range(N)]

        if direction == 1:
            nr = row - 1
            nc = col
            if nr == 0:
                direction = 2
                amount /= 2
        elif direction == 2:
            nr = row + 1
            nc = col
            if nr == N - 1:
                direction = 1
                amount /= 2
        elif direction == 3:
            nr = row
            nc = col - 1
            if nc == 0:
                direction = 4
                amount /= 2
        elif direction == 4:
            nr = row
            nc = col + 1
            if nc == N - 1:
                direction = 3
                amount /= 2

        if data_storage[nr][nc] != 0:
            best_direction = data_storage[nr][nc][0]
            sum_amount = data_storage[nr][nc][1]
            best_micro_amount = data_storage[nr][nc][2]
            if best_micro_amount > amount:
                deq.append((nr, nc, sum_amount + amount, best_direction, k + 1))
                deq.remove((nr, nc, sum_amount, best_direction, k + 1))
                data_storage[nr][nc] = [best_direction, sum_amount + amount, best_micro_amount]
            else:
                deq.append((nr, nc, sum_amount + amount, direction, k + 1))
                deq.remove((nr, nc, sum_amount, best_direction, k + 1))
                data_storage[nr][nc] = [direction, sum_amount + amount, amount]
        
        else:
            deq.append((nr, nc, amount, direction, k + 1))
            data_storage[nr][nc] = [direction, amount, amount]
        
        sv_k = k

    print("#{} {}".format(test_case, result))
            

        
