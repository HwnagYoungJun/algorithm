import sys
import pprint
sys.stdin = open("test.txt")


def multiply_minus(number):
    return number * (-1)


def is_out_side(row, col, n):
    if 0 <= row < n and 0 <= col < n:
        return False
    return True


def ratio_of_scatter_sand_by_direction(direction):
    dr = [0, 0, -1 , 1, -1, -2, 1, 2, -1, 1]
    dc = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1]
    if direction == 0:
        pass
    elif direction == 1:
        dr, dc = list(map(multiply_minus, dc[:])), dr[:]
        # dr = [2, 1, 1, 1, 0, 0, 0, 0, -1, -1]
        # dc = [0, 0, -1, 1, -1, -2, 1, 2, -1, 1]
    elif direction == 2:
        dc =  list(map(multiply_minus, dc))
        # dr = [0, 0, -1 , 1, -1, -2, 1, 2, -1, 1]
        # dc = [2, 1, 1, 1, 0, 0, 0, 0, -1, -1]
    elif direction == 3:
        dr, dc= dc[:], dr[:]
        # dr = [-2, -1, -1, -1, 0, 0, 0, 0, 1, 1]
        # dc = [0, 0, -1, 1]
    
    ratio_list = [0.05, 0.55, 0.10, 0.10, 0.07, 0.02, 0.07, 0.02, 0.01, 0.01]
    
    return (dr, dc, ratio_list)


def scatter_of_sand(row, col, direction):
    result = 0
    n = len(map_list)
    amount_of_sand = map_list[row][col]
    remain_sand = amount_of_sand
    map_list[row][col] = 0
    # print("scatter")
    # print(row, col, direction, amount_of_sand)
    dr, dc, ratio_list = ratio_of_scatter_sand_by_direction(direction)
    # print(row, col, "rowcol")
    for w in range(11):

        # 문제를 잘못이해함으로 인한 긴급 수정
        if w == 1:
            continue
        if w == 10:
            nr = row + dr[1]
            nc = col + dc[1]
            if is_out_side(nr, nc, n):
                # print(nr, nc, "@@@@@@")
                result += remain_sand
            else:
                map_list[nr][nc] += remain_sand
            continue
                
        nr = row + dr[w]
        nc = col + dc[w]
        scattered_sand = int(amount_of_sand * ratio_list[w])
        remain_sand -= scattered_sand
        # print(nr, nc)
        if is_out_side(nr, nc, n):
            # print(nr, nc, scattered_sand)
            result += scattered_sand
        else:
            map_list[nr][nc] += scattered_sand

    return result 


def move_of_tornado(row, col, direction):
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    nr = row + dr[direction]
    nc = col + dc[direction]
    result = 0

    if map_list[nr][nc] != 0:
        result = scatter_of_sand(nr, nc, direction)

    return (nr, nc, result)


def cast_a_tornado(map_list):
    result = 0
    n = len(map_list)
    direction = 0 # 좌 하 우 상 -> 0, 1, 2, 3
    row = n // 2
    col = n // 2

    for turn in range(1, n + 1):

        for _ in range(2):
            for _ in range(turn):
                # print("========================")
                # print(row, col, direction, result)
                row, col, res = move_of_tornado(row, col, direction)
                # pprint.pprint(map_list)
                result += res

            direction += 1
            if direction > 3:
                direction = 0

            if turn == n:
                break
        
    return result


N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]

result = cast_a_tornado(map_list)
print(result)