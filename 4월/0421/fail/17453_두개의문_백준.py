import sys
sys.stdin = open('17453.txt')

def dfs():
    visit = [0 for _ in range()]

n, m = map(int, input().split())

init = 0
temp = list(input())
for i in temp:
    if i == '0' :
        init -= 1
    else:
        init += 1

switch = list()
for i in range(m):
    sw = list(input())
    temp_num = 0
    print(sw)
    for i in sw:
        if i == '0' :
            temp_num -= 1
        else:
            temp_num += 1
    
    switch.append(temp_num)

print(switch)

for i in range(2 * n + 1):
    i -= n
