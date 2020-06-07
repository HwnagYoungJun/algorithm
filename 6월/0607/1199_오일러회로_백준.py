import sys
sys.stdin = open('1199.txt')
sys.setrecursionlimit(10000)

def dfs(n):
    global Euler_circuit
    global E_list
    Euler_circuit.append(n + 1)
    for next_n in conject[n][1]:
        if conject[next_n][0] % 2:
            continue
        if E_list.get((n, next_n)) != None:
            print(E_list)
            print(conject)
            if E_list[(n, next_n)] == 1:
                del E_list[(n, next_n)]
                del E_list[(next_n, n)]
            else:
                E_list[(n, next_n)] -= 1
                conject[n][0] -= 1
                conject[next_n][0] -= 1
                E_list[(next_n, n)] -= 1
            print(next_n)
            dfs(next_n)

N = int(input())
map_list = [list(map(int, input().split())) for _ in range(N)]
conject = {i: [0, []] for i in range(N)}
E_list = dict()
for row in range(N - 1):
    for col in range(row + 1, N):
        if map_list[row][col] != 0:
            value = map_list[row][col]
            conject[row][0] += value
            conject[row][1].append(col)
            conject[col][0] += value
            conject[col][1].append(row)
            E_list[(row, col)] = value
            E_list[(col, row)] = value
print(conject)
is_Euler_circuit = True
for i in range(N):
    if conject[i][0] % 2:
        is_Euler_circuit = False
        break

if not is_Euler_circuit:
    print(-1)
else:
    Euler_circuit = []
    dfs(0)
    print(*Euler_circuit)