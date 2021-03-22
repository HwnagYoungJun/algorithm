import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        answer += 1

        if len(scoville) < 2:
            answer = -1
            break
        
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        c = (a + b * 2)
        heapq.heappush(scoville, c)
        
        d = heapq.heappop(scoville)

        if d >= K:
            break
        else:
            heapq.heappush(scoville, d)

    return answer