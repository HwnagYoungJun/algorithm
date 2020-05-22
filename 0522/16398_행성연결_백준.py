import sys
sys.stdin = open('16398.txt')
import heapq

N = int(input())

maplist = [list(map(int, input().split())) for _ in range(N)]


start = 0
visit = [0 for _ in range(N)]
visit[start] = 1

candidate_list = []
for col in range(N):
    if col != start:
        candidate_list.append((maplist[start][col], col))

heapq.heapify(candidate_list)
result = 0
while candidate_list:
    weight, node = heapq.heappop(candidate_list)
    if visit[node] == 0:
        visit[node] = 1
        result += weight
        for col in range(N):
            if visit[col] == 0:
                if col != node:
                    heapq.heappush(candidate_list,(maplist[node][col], col))

print(result)