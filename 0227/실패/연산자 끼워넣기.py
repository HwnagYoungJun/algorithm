import sys
sys.stdin = open('연산자 끼워넣기.txt')
def perm(n, k, result):
    global my_min
    global my_max
    if n == k:
        cnt = num_list[0]
        for j in range(N - 1):
            if result[j] == '+':
                cnt += num_list[j + 1]
            if result[j] == '-':
                cnt -= num_list[j + 1]
            if result[j] == '*':
                cnt *= num_list[j + 1]
            if result[j] == '/':
                cnt /= num_list[j + 1]
                cnt = int(cnt)
        if cnt > my_max:
            my_max = cnt
        if cnt < my_min:
            my_min = cnt
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            perm(n, k + 1, result + [calc_list[i]])
            visit[i] = 0
N = int(input())
num_list = list(map(int, input().split())) 
calc_list = list() # 더하기, 빼기 등이 있는 리스트
temp_list = list(map(int, input().split()))
for i in range(4):
    for j in range(temp_list[i]):
        if i == 0:
            calc_list.append('+')
        elif i == 1:
            calc_list.append('-')
        elif i == 2:
            calc_list.append('*')
        elif i == 3:
            calc_list.append('/')
visit = [0] * (N - 1) 
my_max = -100000000
my_min = 100000000
perm(N - 1, 0, [])
print(my_max)
print(my_min)