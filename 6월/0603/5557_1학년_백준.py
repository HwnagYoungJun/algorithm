import sys
sys.stdin = open('5557.txt')
import collections

def bfs():
    k = 1
    ans = 0
    while histroy[k]:
        for num, cnt in histroy[k].items():
            if k == T - 1:
                if num == temp[k]:
                    ans += cnt        
                    return ans
            else:
                dn = [temp[k], -temp[k]]
                for w in range(2):
                    nn = dn[w] + num
                    if 0 <= nn <= 20:
                        if histroy[k + 1].get(nn) == None:
                            histroy[k + 1][nn] = cnt
                        else:
                            histroy[k + 1][nn] += cnt
        k += 1
    return ans

T = int(input())
temp = list(map(int, input().split()))
histroy = {i: dict() for i in range(1, T + 1)}
histroy[1][temp[0]] = 1
print(bfs())
