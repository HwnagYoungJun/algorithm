import sys
sys.stdin = open('12851.txt')
import collections  
dx =[1, -1]

def find_sister():
    deq = collections.deque()
    deq.append((subin, 0))
    limit = 2 * sister
    visit = [-1 for _ in range(limit + 1)]
    visit[subin] = 0
    min_time = float('inf')
    count = 0
    
    while deq:
        witch, time = deq.popleft()
        if time > min_time:
            continue
        if witch == sister:
            if time == min_time:
                count += 1
            else:
                min_time = time
                count += 1
        
        dx = [1, -1, witch]
        
        for w in range(3):
            nx = dx[w] + witch
            if w == 0 or w == 2:
                if nx > limit:
                    continue
            else:
                if nx < 0:
                    continue
            if visit[nx] == -1 or time + 1 <= visit[nx]:
                deq.append((nx, time + 1))
                visit[nx] = time + 1
    
    return min_time, count

    
subin, sister = map(int, input().split())

if subin == sister:
    print(0)
    print(1)
elif subin > sister:
    print(subin - sister)
    print(1)
else:
    min_time, count = find_sister()
    print(min_time)
    print(count)