import sys
sys.stdin = open('수영장.txt')

T = int(input())
for test_case in range(1, T + 1):
    day, month, three, year = map(int, input().split())
    use_swimming = list(map(int, input().split()))

    
