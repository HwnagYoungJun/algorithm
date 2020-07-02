import sys
sys.stdin = open('12764.txt')
import heapq


# 1. 시작 순서가 빠른대로 정렬한다.
# 2. 한명씩 빈자리로 출발.
# 3. 전부다 사용 중이라면 새로운 컴퓨터 생성
N = int(input())
soldiers = [list(map(int, input().split())) for _ in range(N)]
soldiers.sort()

computer = dict()
computer_num = 1
pq = []
possible_use = []
for start, end in soldiers:

    if not pq:
        heapq.heappush(pq, (end, computer_num))
        computer[computer_num] = 1
        computer_num += 1
        
    else:
        while pq:
            finish, cn = heapq.heappop(pq)
            if finish > start:
                heapq.heappush(pq, (finish, cn))
                break
            heapq.heappush(possible_use, cn)
        
        if possible_use:
            num = heapq.heappop(possible_use)
            heapq.heappush(pq, (end, num))
            computer[num] += 1
        else:
            heapq.heappush(pq, (end, computer_num))
            computer[computer_num] = 1
            computer_num += 1


print(computer_num - 1)
for i in computer.values():
    print(i, end=' ')