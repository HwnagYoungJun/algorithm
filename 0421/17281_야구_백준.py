import sys
sys.stdin = open('17281.txt')
from itertools import permutations
end = int(sys.stdin.readline())
temp = [list(map(int, sys.stdin.readline().split())) for _ in range(end)]
def play_game(sunbal):
    score = 0
    j = 0
    for i in temp:
        cnt = 0
        b1, b2, b3 = 0, 0, 0
        while cnt < 3:
            if i[sunbal[j]] == 0:
                cnt += 1
            elif i[sunbal[j]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif i[sunbal[j]] == 2:
                score += (b3 + b2)
                b1, b2, b3 = 0, 1, b1
            elif i[sunbal[j]] == 3:
                score += (b3 + b2 + b1)
                b1, b2, b3 = 0, 0, 1
            elif i[sunbal[j]] == 4:
                score += (b3 + b2 + b1 + 1)
                b1, b2, b3 = 0, 0, 0
            j += 1
            if j == 9:
                j = 0

    return score

max_score = float('-inf')

for sunbal in permutations(range(1, 9), 8):
    sunbal = list(sunbal)
    sunbal.insert(3, 0)
    max_score = max(max_score, play_game(sunbal))
print(max_score)