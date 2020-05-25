import sys
sys.stdin = open('상호의 배틀필드.txt')
import collections
def left(row, col, position):
    if 0 <= col - 1< C:
        if battle_field[row][col - 1] == ".":
            return (row, col - 1, 0)
    return (row, col, 0)
def right(row, col, position):
    if 0 <= col + 1 < C:
        if battle_field[row][col + 1] == ".":
            return (row, col + 1, 1)
    return (row, col, 1)
def up(row, col, position):
    if 0 <= row - 1< R:
        if battle_field[row - 1][col] == ".":
            return (row - 1, col, 2)
    return (row, col, 2)
def down(row, col, position):
    if 0 <= row + 1 < R:
        if battle_field[row + 1][col] == ".":
            return (row + 1, col, 3)
    return (row, col, 3)
def shoot(row, col, position):
    if position == 0:
        if col == 0:
            return (row, col, position)
        for w in range(col, -1, -1):
            if battle_field[row][w] == '#':
                return (row, col, position)
            elif battle_field[row][w] == '*':
                battle_field[row][w] = '.'
                return (row, col, position)
        return (row, col, position)
    elif position == 1:
        if col == C:
            return (row, col, position)
        for w in range(col, C):
            if battle_field[row][w] == '#':
                return (row, col, position)
            elif battle_field[row][w] == '*':
                battle_field[row][w] = '.'
                return (row, col, position)
        return (row, col, position)
    elif position == 2:
        if row == 0:
            return (row, col, position)
        for w in range(row, -1, -1):
            if battle_field[w][col] == '#':
                return (row, col, position)
            elif battle_field[w][col] == '*':
                battle_field[w][col] = '.'
                return (row, col, position)
        return (row, col, position)
    elif position == 3:
        if row == R:
            return (row, col, position)
        for w in range(row, R):
            if battle_field[w][col] == '#':
                return (row, col, position)
            elif battle_field[w][col] == '*':
                battle_field[w][col] = '.'
                return (row, col, position)
        return (row, col, position)

T = int(input())
for test_case in range(1, T + 1):
    if test_case != 1:
        print()
    R, C = map(int, input().split())
    battle_field = [list(input()) for _ in range(R)]
    N = int(input())
    temp = input()
    if N == 0:
        print("#{} ".format(test_case),end='')
        for row in range(R):
            if row != 0:
                print()
            for j in battle_field[row]:
                print(j,end='')
        break
    else:
        command_deq = collections.deque()
        for i in temp:
            command_deq.append(i)
        position = 0  # 방향 0 : 좌, 1: 우 2: 상, 3: 하 
        for row in range(R):
            for col in range(C):
                if battle_field[row][col] == '<':
                    position = 0
                    r = row
                    c = col
                elif battle_field[row][col] == '>':
                    position = 1
                    r = row
                    c = col
                elif battle_field[row][col] == '^':
                    position = 2
                    r = row
                    c = col
                elif battle_field[row][col] == 'v':
                    position = 3
                    r = row
                    c = col
        battle_field[r][c] = '.'
        while len(command_deq) != 0:
            command = command_deq.popleft()
            if command == 'L':
                value = left(r, c, position)
            elif command == 'R':
                value = right(r, c, position)
            elif command == 'U':
                value = up(r, c, position)
            elif command == 'D':
                value = down(r, c, position)
            elif command == 'S':
                value = shoot(r,c, position)
            r, c, position = value
        if position == 0:
            battle_field[r][c] = '<'
        elif position == 1:
            battle_field[r][c] = '>'   
        elif position == 2:
            battle_field[r][c] = '^'    
        elif position == 3:
            battle_field[r][c] = 'v'
        print("#{} ".format(test_case),end='')
        for row in range(R):
            if row != 0:
                print()
            for j in battle_field[row]:
                print(j,end='')