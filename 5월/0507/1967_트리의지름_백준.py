import sys
sys.stdin = open('1967.txt')

def dijkstra(num, mode):
    
    dijk = [float('inf') for _ in range(n + 1)]
    dijk[num] = 0
    dijk[0] = -1
    visit = [0 for _ in range(n + 1)]
    visit[num] = 1
    index = num

    while True:

        for node, dist in tree[index]:
            if visit[node] == 0:
                via = dijk[index] + dist
                if via < dijk[node]:
                    dijk[node] = via

        visit[index] = 1
        min_dist = float('inf')

        for node in range(1, n + 1):
            if dijk[node] < min_dist and visit[node] == 0:
                min_dist = dijk[node]
                index = node
        
        if min_dist == float('inf'):
            break
    
    if mode == 'first':
        return dijk.index(max(dijk))

    elif mode == 'second':
        return max(dijk)

n = int(input())

# 1. 연결리스트로 입력받기
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    i1, i2, dist = map(int, input().split())
    tree[i1].append((i2, dist))
    tree[i2].append((i1, dist))

# 2. 다익스트라를 두번사용하자
print(dijkstra(dijkstra(1, 'first'), 'second'))