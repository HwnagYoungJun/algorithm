import sys
sys.stdin = open('5203.txt')

def straight(g):
    global winner
    if g[-1] - g[-2] == 1 and g[-2] - g[-3] == 1:
        if g == a:
            winner = 1
        else:
            winner = 2
    elif g[-1] - g[-2] == -1 and g[-2] - g[-3] == -1:
        if g == a:
            winner = 1
        else:
            winner = 2
    return

def triple(g, n):
    global winner
    if n == 1:
        if g == 'a':
            if acard[n - 1] != 0 and acard[n + 1] != 0:
                winner = 1
            elif acard[1] != 0 and acard[2] != 0 and acard[3] != 0:
                winner = 1
        else:
            if bcard[n - 1] != 0 and bcard[n + 1] != 0:
                winner = 2
            elif bcard[1] != 0 and bcard[2] != 0 and bcard[3] != 0:
                winner = 2
    elif n == 8:
        if g == 'a':
            if acard[n - 1] != 0 and acard[n + 1] != 0:
                winner = 1
            elif acard[7] != 0 and acard[6] != 0 and acard[8] != 0:
                winner = 1
        else:
            if bcard[n - 1] != 0 and bcard[n + 1] != 0:
                winner = 2
            elif bcard[6] != 0 and bcard[7] != 0 and bcard[8] != 0:
                winner = 2
    elif 2 <= n <= 7:
        if g == 'a':
            if acard[n - 1] != 0 and acard[n + 1] != 0:
                winner = 1
            elif acard[n + 1] != 0 and acard[n + 2] != 0:
                winner = 1
            elif acard[n - 2] != 0 and acard[n - 1] != 0:
                winner = 1
        else:
            if bcard[n - 1] != 0 and bcard[n + 1] != 0:
                winner = 2
            elif bcard[n + 1] != 0 and bcard[n + 2] != 0:
                winner = 2
            elif bcard[n - 2] != 0 and bcard[n - 1] != 0:
                winner = 2
    return

    
T = int(input())
for test_case in range(1, T + 1):
    card = list(map(int, input().split()))

    acard = [0 for _ in range(10)]
    bcard = [0 for _ in range(10)]
    for i in range(4):
        if i % 2 == 0:
            acard[card[i]] += 1
        else:
            bcard[card[i]] += 1
    
    a = [card[0], card[2]]
    b = [card[1], card[3]]
    winner = 0

    for i in range(4, 12):
        print(i)
        if i % 2 == 0:
            a.append(card[i])
            straight(a)
            if winner == 0:
                triple('a', card[i])
        else:
            b.append(card[i])
            straight(b)
            bcard[card[i]] += 1
            if winner == 0:
                triple('b', card[i])
        if winner != 0:
            break
    
    print("#{} {}".format(test_case, winner))