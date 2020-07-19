def solution(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2[0])
    
    answer = [[0 for _ in range(len2)] for _ in range(len1)]
    for row in range(len1):
        for col in range(len2):
            answer[row][col] =  multi(row, col, arr1, arr2, len(arr2))
    
    return answer

def multi(r, c, arr1, arr2, lenlen):
    res = 0
    
    for i in range(lenlen):
        res += arr1[r][i] * arr2[i][c]
    
    return res