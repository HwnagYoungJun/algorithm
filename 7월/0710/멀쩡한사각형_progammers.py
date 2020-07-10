def solution(w,h):
    answer = w * h
    c = gcd(w, h)
    a = w / c
    b = h / c
    
    one_block = (a + b) - 1

    return answer - c * (one_block)

def gcd(a, b):
    
    while b > 0:
        a, b = b, a % b
        
    return a