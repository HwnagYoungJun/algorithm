import sys
sys.stdin = open('1043.txt')

def so(n):
    for j in people[n]:
        if p[j] == 0:
            p[j] = 1
            so(j)

N, M = map(int, input().split())

people = [{i} for i in range(N + 1)]
temp = list(map(int, input().split()))[1:]

party = [list(map(int, input().split())) for _ in range(M)]

for i in party:
    i = i[1:]
    for j in i:
        people[j] |= set(i)

p = [0 for _ in range(N + 1)]

for i in temp:
    so(i)

result = 0
for i in party:
    for j in range(1, len(i)):
        if p[i[j]] == 1:
            break
    else:
        result += 1

print(result)