import sys
sys.stdin = open('3425.txt')


# Error 경우
# 1. 스택에 숫자가 없을 때
# 2. 0으로 나누었을 때
# 3. 연산의 절댓값이 10**9를 넘어갈 때
# 4. 모든 수행이 종료 되었을 때 스택에 저장되어 있는 숫자가 1개가 아니라면

# 음수 나눗셈은 나누는 수를 절댓값 한 뒤 나눈다.


def command(cmd, stack):


    if len(cmd) == 2:
        _, X = cmd
        stack.append(int(X))

    else:  
        cmd = ''.join(cmd)
        if cmd == 'POP':
            if not stack:
                return True
            stack.pop()

        elif cmd == "INV":
            if not stack:
                return True
            stack[-1] *= -1

        elif cmd == 'DUP':
            if not stack:
                return True
            stack.append(stack[-1])

        elif cmd == 'SWP':
            if len(stack) < 2:
                return True
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif cmd == 'ADD':
            if len(stack) < 2:
                return True
            a = stack.pop()
            b = stack.pop()

            if abs(a + b) > 10 ** 9:
                return True 
            stack.append(a + b)

        elif cmd == 'SUB':
            if len(stack) < 2:
                return True
            a = stack.pop()
            b = stack.pop()
            if abs(b - a) > 10 ** 9:
                return True 
            stack.append(b - a)

        elif cmd == 'MUL':
            if len(stack) < 2:
                return True
            a = stack.pop()
            b = stack.pop()
            if abs(a * b) > 10 ** 9:
                return True 
            stack.append(a * b)

        elif cmd == 'DIV':
            if len(stack) < 2:
                return True
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return True 
            if a < 0 or b < 0:
                c = abs(b) // abs(a)
                if a * b  <= 0:
                    c *= -1
                stack.append(c)
            else:
                stack.append(b // a)

        elif cmd == 'MOD':
            if len(stack) < 2:
                return True
            a = stack.pop()
            b = stack.pop()
            if a == 0:
                return True 
            if a < 0 or b < 0:
                c = abs(b) % abs(a)
                if b < 0:
                    stack.append(-c)
                else:
                    stack.append(c)
            else:
                stack.append(b % a)

    return False
    

while True:
    program = []
    init_input = list(input().split())

    if init_input == ['QUIT']:
        break
    
    if init_input == ['END']:
        N = int(input())
        for _ in range(N):
            print(int(input()))
        trash_input = input()
        print()
        continue


    program.append(init_input)

    while True:
        temp = list(input().split())
        if temp == ['END']:
            break
        program.append(temp)

    N = int(input())
    for _ in range(N):
        stack = []
        start = int(input())

        stack.append(start)
        program_over = False

        for cmd in program:
            over = command(cmd, stack)
            if over:
                program_over = True
                break

        if len(stack) != 1:
            program_over = True
        if program_over:
            print('ERROR')
        else:
            print(stack[0])
    
    trash_input = input()
    print()