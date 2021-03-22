def solution(prices):
    len_p = len(prices)
    answer = [0 for _ in range(len_p)]

    for i in range(len_p - 1):
        for j in range(0, i + 1):
            if prices[j] == float('inf'):
                continue
            if prices[j] <= prices[i]:
                answer[j] += 1
            else:
                prices[j] = float('inf')
    return answer