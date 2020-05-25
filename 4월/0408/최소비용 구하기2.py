import sys
sys.stdin = open('최소비용 구하기2.txt')
import collections

def bfs():
    global min_cost
    global min_list
    visit = [float('inf') for i in range(n + 1)]
    deq = collections.deque()
    for i in range(len(cityCanGo[startCity])):
        eend, ccost = cityCanGo[startCity][i]
        deq.append((eend, ccost, [startCity, eend]))
        
    while len(deq) != 0:
        nextCity, costSum, temp_foot = deq.popleft()
        
        if costSum < min_cost:
            if nextCity == endCity:
                min_cost = costSum
                min_list = temp_foot
        
        for j in range(len(cityCanGo[nextCity])):
            goCity, bbcost = cityCanGo[nextCity][j]
            if goCity in temp_foot:
                continue
            else:
                if min_cost <= costSum + bbcost:
                    continue
                
                if goCity == endCity:
                    min_cost = costSum + bbcost
                    min_list = temp_foot + [goCity]
                else:
                    if visit[goCity] < costSum + bbcost:
                        continue
                    else:
                        visit[goCity] = costSum + bbcost
                        deq.append((goCity, costSum + bbcost, temp_foot + [goCity]))

n = int(input())
m = int(input())

cityCanGo = [[] for i in range(n + 1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    cityCanGo[start].append((end, cost))

startCity, endCity = map(int, input().split())

min_cost = float('inf')
min_list = set()

bfs()
if startCity == endCity:
    min_cost = 0
    min_list = {startCity}
    
print(min_cost)
print(len(min_list))
print(*min_list)