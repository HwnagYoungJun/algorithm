import sys
sys.stdin = open('1504.txt')

def dijkstra(start, n1, n2):

    # 최단거리 리스트
    dijk = [float('inf') for _ in range(N + 1)]
    # 시작점은 가중치 0
    dijk[start] = 0
    # 방문확인 리스트
    visit = [0 for _ in range(N + 1)]
    # 시작점은 바로 방문확인
    visit[start] = 1
    # dot은 현재의 정점이다. 시작할때는 시작점으로 지정한다
    dot = start
    # 다익스트라 알고리즘은 while문으로 짜는게 제일 편한것 같다.
    while True:

        # 1. 현재의 정점에서 갈수 있는 정점을 체크하고 그 정점과의 거리를 최신화 시켜준다.
        for w in range(len(route[dot])):
            # route[dot]에는 dot에서 갈수있는 정점들과 가중치가 담겨있다.
            next_dot, value = route[dot][w]
            # 방문확인이 되지않은 정점만 가면 된다.
            if visit[next_dot] == 0:
                # via라는 변수에 dot의 가중치와 value를 더해준다.
                via = dijk[dot] + value
                # 다음 정점에 담긴 최단거리가 via보다 크다면 최신화 시켜준다.
                if via < dijk[next_dot]:
                    dijk[next_dot] = via

        # 방문확인 해준다. (여기해준 이유는 내가 여기하는 하는게 편해서이기 때문이다. 어디써도 크게 상관은 없는것 같다.)
        visit[dot] = 1

        # 2. 시작점에서(바뀌지 않는다.) 가장 가중치가 짧은곳으로 가서 다음 단계를 준비한다.
        # 최단거리 리스트를 탐색할 것이기 떄문에 범위는 최단거리 리스트의 범위이다.
        # 2. 를 시작하기 전에 min_dist를 지정해줘서 비교할 값을 만들어 둔다.
        min_dist = float('inf')
        for w in range(1, N + 1):
            # 방문확인이 되지 않은곳만 체크하면 된다.
            if visit[w] == 0:
                # 비교할 값과 최단거리를 비교해 최신화 시켜준다
                if min_dist > dijk[w]:
                    min_dist = dijk[w]
                    # 만약 최신화 되었다면 그 떄의 정점도 저장해둔다.
                    dot = w
        


        # !return 조건!
        # 2. 과정에서 최단거리가 최신화 되지않는 다는 이야기는 더 이상 갈 곳이 없기 때문에 탐색을 마무리한다.
        # 바뀌지 않았으면 갈 곳이 없는 것이다.
        if min_dist == float('inf'):
            break
    
    return dijk[n1], dijk[n2]




N, E = map(int, input().split())

route = [[] for _ in range(N + 1)]
for i in range(E):
    a, b, e = map(int, input().split())
    # 양방향 체크
    route[a].append((b, e))
    route[b].append((a, e))

v1, v2 = map(int, input().split())

r1, r2= dijkstra(1, v1, v2)
rN1, rv2 = dijkstra(v1, N, v2)
rN2, rv1 = dijkstra(v2, N, v1)
if min(r1 + rN2 + rv2, r2 + rN1 + rv1) == float('inf'):
    print(-1)
else:
    print(min(r1 + rN2 + rv2, r2 + rN1 + rv1))