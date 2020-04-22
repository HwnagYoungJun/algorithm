import sys
sys.stdin = open('1912.txt')

n = int(input())
su_list = list(map(int, input().split()))



for i in range(1, n):
    if su_list[i - 1] > 0:
        su_list[i] += su_list[i - 1] 
print(max(su_list))