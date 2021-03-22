import sys
sys.stdin = open("세상의 모든 팰린드롬.txt")

T = int(input())
for test_case in range(1, T + 1):
    inp_ruk = input()
    result = 'Not exist'
    if '?' not in inp_ruk:
        if inp_ruk == inp_ruk[::-1]:
            result = 'Exist'
    else:
        middle = int(len(inp_ruk))
        for i in range(middle):
            if inp_ruk[i] == '?' or inp_ruk[-i - 1] == '?':
                pass
            elif inp_ruk[i] != inp_ruk[-i - 1]:
                break
        else:
            result = 'Exist'
    print("#{} {}".format(test_case, result))