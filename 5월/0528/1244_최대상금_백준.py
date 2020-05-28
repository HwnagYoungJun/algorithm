import sys
sys.stdin = open('1244.txt')

def dfs(k, price):
    global visit
    global max_price
    if price in visit[k]:
        return
    else:
        visit[k].append(price)
    if k == change:
        if max_price < int(''.join(price)):
            max_price = int(''.join(price))
        return
    
    for i in range(len_n - 1):
        for j in range(i + 1, len_n):
            c_price = price[:]
            c_price[i], c_price[j] = c_price[j], c_price[i]
            dfs(k + 1, c_price)

T = int(input())
for test_case in range(1, T + 1):
    temp, change = map(int, input().split())
    number = list(str(temp))
    len_n = len(number)
    max_price = float('-inf')
    visit = [[] for _ in range(change + 1)]
    dfs(0, number)
    print("#{} {}".format(test_case, max_price))
        