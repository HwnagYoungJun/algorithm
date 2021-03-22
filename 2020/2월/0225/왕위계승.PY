import sys
import collections
sys.stdin = open('왕위계승.txt')
def bfs(name, blood):
    deq.append((name, blood))

    while len(deq) != 0:
        bname, bblood = deq.popleft()
        for w in range(N):
            son = royalfamily[w][0]
            father = royalfamily[w][1]
            mother = royalfamily[w][2]
            if (father == bname or mother == bname):
                royalblood[son] += bblood / 2
                visit[son] += 1
                deq.append((son, bblood / 2))

N, M = map(int, input().split())
king = input()
royalfamily = [list(input().split()) for i in range(N)]
candidate = []
for i in range(M):
    candidate.append(input())
royalblood = {royalfamily[i][0]: 0 for i in range(N)}
visit = {royalfamily[i][0]: 0 for i in range(N)}
deq = collections.deque()

bfs(king, 1)
chk = 0
result = ''
for i in candidate:
    if i in royalblood and chk < royalblood[i]:
        chk = royalblood[i]
        result = i
print(result)


