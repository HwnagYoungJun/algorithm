import heapq

def solution(jobs):
    len_j = len(jobs)
    time = 0
    end = -1
    pq = []

    count = 0
    answer = 0

    while count < len_j:
        for i in jobs:
            if end < i[0] <= time:
                answer += time - i[0]
                heapq.heappush(pq, i[1])

        if pq:
            answer += len(pq) * pq[0]
            end = time
            time += heapq.heappop(pq)
            count += 1
        else:
            time += 1
    return answer // len_j

jobs = [[0, 3], [1, 9], [2, 6]]
solution(jobs)