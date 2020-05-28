import sys
sys.stdin = open('10775.txt')

G = int(input())
P = int(input())

airport = dict()

max_plane = 0

sago = False

parent = {i: i for i in range(1, G + 1)}
for plane in range(1, P + 1):

    if sago:
        break

    this_gate = int(input())
    temp = parent[this_gate]
    for i in range(temp, 0, -1):
        # print(airport.get(i))
        if airport.get(i) == None:
            airport[i] = plane
            parent[this_gate] = i
            max_plane += 1
            break
    else:
        sago = True

print(max_plane)