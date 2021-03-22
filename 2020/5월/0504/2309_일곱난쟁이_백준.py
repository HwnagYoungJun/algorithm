import sys
sys.stdin = open('2309.txt')


def my_perm(num, k, hap, sett):
    global result
    if hap > 100:
        return
    if k == 7 and hap == 100:
        result = sett
        return

    for i in range(num, 9):
        if small_man[i] not in sett:
            my_perm(i, k + 1, hap + small_man[i], sett + [small_man[i]])

    
small_man = list()
for i in range(9):
    small_man.append(int(input()))


result = list()
for i in range(3):
    visit = [0 for _ in range(9)]
    my_perm(i, 1, small_man[i], [small_man[i]])

result.sort()
for i in result:
    print(i)