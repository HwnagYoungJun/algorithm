import sys
sys.stdin = open('개똥벌레.txt')

N, H = map(int, input().split())

top = [0 for i in range(H + 1)]
bottom = [0 for i in range(H + 1)]
for i in range(N):
    lenght = int(input())
    
    if i % 2 == 0:  # 짝수
        bottom[lenght] += 1
    elif i % 2 == 1: # 홀수
        top[lenght] += 1

for i in range(len(top) - 2, 0, -1):
    top[i] += top[i + 1]
for i in range(len(bottom) - 2, 0, -1):
    bottom[i] += bottom[i + 1]

for i in range(1, len(top)):
    top[i] += bottom[-i]

top[0] = float('inf')
min_value = min(top)
count = top.count(min_value)

print("{} {}".format(min_value, count))