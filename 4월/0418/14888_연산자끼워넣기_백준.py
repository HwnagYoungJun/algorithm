def dfs(value, k, add, sub, multi, division):
    global max_value
    global min_value

    if k == N:
        if max_value < value:
            max_value = value
        
        if min_value > value:
            min_value = value
        return
    
    for w in range(4):
        if w == 0:
            if add != 0:
                dfs(value + A[k], k + 1, add - 1, sub, multi, division)
        if w == 1:
            if sub != 0:
                dfs(value - A[k], k + 1, add, sub - 1, multi, division) 
        if w == 2:
            if multi != 0:
                dfs(value * A[k], k + 1, add, sub, multi - 1, division) 
        if w == 3:
            if division != 0:
                dfs(int(value / A[k]), k + 1, add, sub, multi, division - 1) 




N = int(input())

A = list(map(int, input().split()))

plus, minus, time, divide = map(int, input().split())

max_value = float('-inf')
min_value = float('inf')
dfs(A[0], 1, plus, minus, time, divide)

print(max_value)
print(min_value)