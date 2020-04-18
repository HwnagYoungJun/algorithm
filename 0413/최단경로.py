import sys
sys.stdin = open('최단경로.txt')

def dijkstra(K, V, graph):
    INF = float('inf')
    # s는 해당 노드를 방문 했는지 여부를 저장하는 변수이다
    visit = [False] * (V + 1)
    # d는 memoization을 위한 array이다. d[i]는 정점 K에서 i까지 가는 최소한의 거리가 저장되어 있다.
    memo = [INF] * (V + 1)
    memo[K] = 0

    while True:
        m = INF
        N = -1

        # 방문하지 않은 노드 중 d값이 가장 작은 값을 선택해 그 노드의 번호를 N에 저장한다.
        # 즉, 방문하지 않은 노드 중 K 정점과 가장 가까운 노드를 선택한다.
        for j in range(1, V + 1):
            if visit[j] == 0 and m > memo[j]:
                m = memo[j]
                N = j

        # 방문하지 않은 노드 중 현재 K 정점과 가장 가까운 노드와의 거리가 INF 라는 뜻은
        # 방문하지 않은 남아있는 모든 노드가 A에서 도달할 수 없는 노드라는 의미이므로 반복문을 빠져나간다.
        if m == INF:
            break

        # N번 노드를 '방문'한다.
        # '방문'한다는 의미는 모든 노드를 탐색하며 N번 노드를 통해서 가면 더 빨리 갈 수 있는 노드가 있는지 확인하고,
        # 더 빨리 갈 수 있다면 해당 노드(노드의 번호 j라고 하자)의 d[j]를 업데이트 해준다.
        visit[N] = True

        for j in range(1, V + 1):
            if visit[j] != 0: 
                continue

            via = memo[N] + graph[N][j]
            
            if memo[j] > via:
                memo[j] = via

    return memo

V, E = map(int, input().split())
K = int(input())
INF = sys.maxsize
graph = [[INF] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

for d in dijkstra(K, V, graph):
    print(d if d != INF else "INF")