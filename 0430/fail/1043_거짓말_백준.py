N, M = map(int, input().split())
known = set(list(map(int, input().split()))[1:])
unknown = set()
party = [0 for _ in range(M + 1)]

for i in range(1, M + 1):

    party[i]= set(list(map(int, input().split()))[1:])

max_party = 0

for i in range(1, M + 1):
    if party[i] & known == True and party[i] & unknown == False:
        known = known | party[i]

    else:
        max_party += 1
        unknown = unknown | party[i]

print(max_party)
