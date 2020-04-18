import sys
sys.stdin = open("스타일리쉬 들여쓰기.txt")

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())
    brackets = [0, 0, 0, 0, 0, 0]  # (, ), {, }, [, ]
    ABC_list = set()
    result = [0]
    for i in range(1, 21):
        for j in range(1, 21):
            for k in range(1, 21):
                ABC_list.add((i, j, k))
    for i in range(p):
        master_string = input()
        swich = True
        count = 0
        for j in master_string:
            if swich == True:
                if j != '.':
                    if i != 0:
                        swich = False
                        copy_temp = ABC_list.copy()
                        for tuple_ABC in ABC_list:
                            A, B, C = tuple_ABC
                            if count != A *(brackets[0] - brackets[1]) + B * (brackets[2] - brackets[3]) + C * (brackets[4] - brackets[5]):
                                copy_temp.remove(tuple_ABC)
                        ABC_list = copy_temp
                else:
                    count += 1
                    continue
            if j == '(':
                brackets[0] += 1
            elif j == ')':
                brackets[1] += 1
            elif j == '{':
                brackets[2] += 1
            elif j == '}':
                brackets[3] += 1
            elif j == '[':
                brackets[4] += 1
            elif j == ']':
                brackets[5] += 1

    brackets = [0, 0, 0, 0, 0, 0]
    for i in range(q):
        my_string = input()
        swich = True
        for j in my_string:
            if swich == True:
                if j != '.':
                    if i != 0:
                        swich = False
                        tt = True
                        for ABC in ABC_list:
                            A, B, C = ABC
                            if tt == True:
                                sv_tab = A *(brackets[0] - brackets[1]) + B * (brackets[2] - brackets[3]) + C * (brackets[4] - brackets[5])
                                tt = False
                            else:
                                tab = A *(brackets[0] - brackets[1]) + B * (brackets[2] - brackets[3]) + C * (brackets[4] - brackets[5])
                                if sv_tab != tab:
                                    sv_tab = -1
                                    break
                        result.append(sv_tab)
                else:
                    continue
            if j == '(':
                brackets[0] += 1
            elif j == ')':
                brackets[1] += 1
            elif j == '{':
                brackets[2] += 1
            elif j == '}':
                brackets[3] += 1
            elif j == '[':
                brackets[4] += 1
            elif j == ']':
                brackets[5] += 1
    
    print("#{}".format(test_case), *result)

