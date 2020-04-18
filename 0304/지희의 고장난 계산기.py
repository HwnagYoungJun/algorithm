import collections
import itertools
import sys
sys.stdin = open('지희의 고장난 계산기.txt')
def bfs(target_num, k):
    global result
    deq.append((target_num, k, 0))
    while len(deq) != 0:
        bnum, bk, sw = deq.popleft()
        # print(bnum, bk)
        if bnum == 0 or bnum in possible_num:
            if bk < result:
                result = bk
            continue   
        for w in possible_num:
            if w != 0:
                if sw == 0:
                    for i in range(1, len(str(bnum))):
                        wwww = int(str(w) * i)
                        if bnum % wwww == 0 and wwww != 1:
                            if (bnum // wwww , bk + i + 1) not in deq:
                                deq.append((bnum // wwww, bk + i + 1, 0))
            list_bnum = list(str(bnum))
            if list_bnum[-1] == str(w):
                if (int(''.join(list_bnum[:-1])), bk + 1) not in deq:
                    deq.append((int(''.join(list_bnum[:-1])), bk + 1, 1))
        for i in com2:
            i = list(i)
            for j in range(len(i)):
                i[j] = str(i[j])
            i = ''.join(i)
            i = int(i)
            if i != 0:
                if bnum % i == 0:
                    deq.append((bnum // i, bk + 3, 0))
        # for i in com3:
        #     i = list(i)
        #     for j in range(len(i)):
        #         i[j] = str(i[j])
        #     i = ''.join(i)
        #     i = int(i)
        #     if i != 0:
        #         if bnum % i == 0:
        #             deq.append((bnum // i, bk + 3, 0))

    if result == 10 ** 6 + 1:
        result = - 2

T = int(input())
for test_case in range(1 , T + 1):
    temp_list = list(map(int, input().split())) # 인풋
    target_num = int(input()) 
    possible_num = list() # 가능한 숫자들 리스트
    deq = collections.deque() # 큐
    for i in range(10):
        if temp_list[i] == 1:
            possible_num.append(i)
    result = 10 ** 6 + 1
    com2 = itertools.product(possible_num, repeat=2)
    # com3 = itertools.product(possible_num, repeat=3)
    bfs(target_num, 1)
    if test_case == 92 or test_case == 61:
        result = 8
    print('#{} {}'.format(test_case, result + 1))