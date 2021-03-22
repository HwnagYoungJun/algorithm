import sys
sys.stdin = open('1916.txt')
input = sys.stdin.readline

def dijkstra():
    dijk = [float('inf') for _ in range(N + 1)]
    dijk[start] = 0
    visit = [i for i in range(1, N + 1)]

    index = start
    while True:

        for i in range(len(bus_info[index])):
            d, c = bus_info[index][i]
            if d in visit:
                via = dijk[index] + c
                if via < dijk[d]:
                    dijk[d] = via
        
        visit.remove(index)

        min_cost = float('inf')
        for j in visit:
            if min_cost > dijk[j]:
                min_cost = dijk[j]
                index = j
        if min_cost == float('inf'):
            break

    return dijk[end]

N = int(input())
M = int(input())
bus_info = [[] for _ in range(N + 1)]

for i in range(M):
    num1, num2, cost = map(int ,input().split())
    bus_info[num1].append((num2, cost))

start, end = map(int, input().split())

print(dijkstra())
