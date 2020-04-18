import sys
sys.stdin = open('연속합.txt')

n = int(input())
수열 = list(map(int, input().split()))

max_value = float('-inf')

for start in range(n):
    if 수열[start] > 0:
        if start != 0:
            if 수열[start - 1] < 0:
                memo = 0 
                for end in range(start, n):
                    memo += 수열[end]

                    if memo > max_value:
                        max_value = memo
        elif start == 0:
            memo = 0 
            for end in range(start, n):
                memo += 수열[end]

                if memo > max_value:
                    max_value = memo

print(max_value)