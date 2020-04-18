import sys
sys.stdin = open('수영장.txt')
def good_swim(mon, pp):
    global price
    if price <= pp:
        return
    if mon >= 13:
    	price = pp
    	return
    for w in range(3):
        if use_swimming[mon] == 0:
            good_swim(mon + 1, pp)
        else:
            if w == 0:
                good_swim(mon + 1, pp + (day * use_swimming[mon]))
            elif w == 1:
                good_swim(mon + 1, pp + month)
            elif w == 2:
                good_swim(mon + 3, pp + three)

T = int(input())
for test_case in range(1, T + 1):
    day, month, three, year = map(int, input().split())
    use_swimming = [0] + list(map(int, input().split()))
    price = 10000000
    good_swim(1, 0)
    if price > year:
        price = year
    print('#{} {}'.format(test_case, price))