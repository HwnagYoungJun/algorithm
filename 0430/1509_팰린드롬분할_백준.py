import sys
sys.stdin = open('1509.txt')
sys.setrecursionlimit(100000)

def dfs(n, count):
    global min_division

    if count > min_division:
        return
    if n == length:
        if count < min_division:
            min_division = count
            return

    for i in range(length + 2, n, -1):

        if string[n:i] == string[n:i][::-1]:
            # print(string[n:i])
            # print(string[n:i][::-1])
            dfs(i, count + 1)

string = input()
# string = string.strip('\\n')
length = len(string)
min_division = float('inf')

dfs(0, 0)

print(min_division)

