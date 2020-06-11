import sys
sys.stdin = open('1135.txt')
import heapq

def find_minsik(man, zim):
    head = company[man][0]
    if head == -1:
        return
    else:
        conj_junior[head] += zim
        find_minsik(head, zim)

def bfs():
    visit = {i: False for i in range(N)}
    visit[0] = True
    pq = []
    pq.append((0, 0)) # (시간, 사람)
    heapq.heapify(pq)
    call_member = 0
    while pq:
        time, person = heapq.heappop(pq)
        call_member += 1
        if call_member == N:
            return time
        for i in range(len(company[person][1])):
            next_person = company[person][1][i][1]
            if not visit[next_person]:
                heapq.heappush(pq, (time + i + 1, next_person))
    

N = int(input())
temp = list(map(int, input().split()))

company = {i: [-1, []] for i in range(N)}
conj_junior = {i : 0 for i in range(N)}
for junior in range(N):
    senior = temp[junior]
    company[junior][0] = senior
    if senior != -1:
        company[senior][1].append(junior)

for i in range(N):
    if not company[i][1]:
        continue
    max_junior = float('-inf')
    for j in company[i][1]:
        max_junior = max(conj_junior[j] + 1, max_junior)
    conj_junior[i] += max_junior
    find_minsik(i, max_junior)

for i in range(N):
    for j in range(len(company[i][1])):
        company[i][1][j] = (conj_junior[company[i][1][j]], company[i][1][j])

for i in range(N):
    company[i][1].sort(reverse=True)

print(bfs())