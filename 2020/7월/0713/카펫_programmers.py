def solution(brown, yellow):
    answer = []
    brown += 2
    brown //= 2
    brown += 1
    # b1: 가로, b2: 세로
    b1 = brown - 3
    b2 = 3
    
    while True:
        
        if (b1 - 2) * (b2 - 2) == yellow:
            break
            
        b1 -= 1
        b2 += 1
    
    answer = [b1, b2]
    return answer