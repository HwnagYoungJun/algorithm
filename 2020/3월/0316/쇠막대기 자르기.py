import sys
sys.stdin = open('쇠막대기 자르기.txt')

T = int(input())
for test_case in range(1, T + 1):
    temp_list = input()
    stack = list()
    count = 0
    gil_2 = len(temp_list)
    razer = [0] * gil_2
    result = 0 
    for i in range(gil_2):
        razer[i] += count
        if temp_list[i] == '(':
            if i != gil_2 - 1:
                if temp_list[i + 1] != ')':
                    stack.append(i)
                elif temp_list[i + 1] == ')':
                    count += 1
        elif temp_list[i] == ')' and temp_list[i - 1] != '(':
            stack.append(i)
            end = stack.pop()
            start = stack.pop()
            result += (razer[end] - razer[start] + 1)
    print("#{} {}".format(test_case, result))
