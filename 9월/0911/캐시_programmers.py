import collections

def solution(cacheSize, cities):
    answer = 0
    cache_list = collections.deque()
    cnt = 0

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        cnt += 1
        city = city.upper()
        if city in cache_list:
            answer += 1
            if cnt > cacheSize:
                cache_list.remove(city)
                cache_list.append(city)
            else:
                cache_list.append(city)
        else:
            answer += 5

            if cnt > cacheSize:
                cache_list.popleft()
                cache_list.append(city)
            else:
                cache_list.append(city)
        
    return answer