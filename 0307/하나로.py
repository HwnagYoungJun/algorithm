import sys
sys.stdin = open('하나로.txt')
import math

def calc(x1, y1, x2, y2):
    return (((((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5) ** 2) * tax

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 섬의 갯수
    island_x = list(map(int, input().split()))
    island_y = list(map(int, input().split()))
    tax = float(input( ))
    final_final_cost = float('inf')
    for a in range(N):
        print()
        print(a)
        print()
        island_x[0], island_x[a] = island_x[a], island_x[0]
        island_y[0], island_y[a] = island_y[a], island_y[0]
        final_cost = 0
        for i in range(N - 1):
            if i == 0:
                copy_x = island_x[::]
                copy_y = island_y[::]
            min_cost = float('inf')
            for j in range(i + 1, N):
                cost = calc(copy_x[i], copy_y[i], copy_x[j], copy_y[j])
                if cost < min_cost:
                    min_cost = cost
                    mini = j
            copy_x[i + 1], copy_x[mini] = copy_x[mini], copy_x[i + 1]
            copy_y[i + 1], copy_y[mini] = copy_y[mini], copy_y[i + 1]

            final_cost += calc(copy_x[i], copy_y[i], copy_x[i + 1], copy_y[i + 1])
            print(i, 'iu', final_cost, final_final_cost)
            
            if final_cost > final_final_cost:
                print('탈출!') 
                break
        print(final_cost)
        print(copy_x)
        print(copy_y)
        final_final_cost = final_cost
    print('#{} {}'.format(test_case, round(final_final_cost)))
    
