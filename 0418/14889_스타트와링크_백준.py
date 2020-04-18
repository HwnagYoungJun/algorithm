import sys
sys.stdin = open('14889.txt')

# 조합을 사용하여 start팀을 뽑는 함수
# DFS를 베이스로 함

def my_collection(n, k, foot_step):  # k : 깊이, # foot_step : 이때 까지 담긴 숫자들
    global min_value
    
    visit = [0 for _ in range(N)]
    visit[n] = k

    if k == N / 2:
        # DFS는 여기서 하고싶은걸 하면 된다.
        start_stat = 0
        link_stat = 0
        for row in range(N):
            for col in range(N):
                if row in foot_step and col in foot_step:
                    if row != col:
                        start_stat += soccer[row][col]
        
                elif row not in foot_step and col not in foot_step:
                    if row != col:
                        link_stat += soccer[row][col]
        if abs(link_stat - start_stat) < min_value:
            min_value = abs(link_stat - start_stat)
        return

    for next_num in range(n, N):
        if visit[next_num] == 0:
            visit[next_num] = 1
            my_collection(next_num, k + 1, foot_step | {next_num})
            visit[next_num] = 0  # 나갈 때 방문체크 해제 필수

N = int(input())

soccer = [list(map(int, input().split())) for _ in range(N)]


min_value = float('inf')
my_collection(0, 1, {0})

print(min_value)