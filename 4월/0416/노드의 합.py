import sys
sys.stdin = open("노드의 합.txt")

T = int(input())
for test_case in range(1, T + 1):
    # N개의 노드, L 루트, M개의 번호
    N, M, L = map(int, input().split())

    tree = [0 for _ in range(N + 1)]

    for i in range(M):
        node, num = map(int, input().split())

        tree[node] = num
    
    for j in range(N, 0, -1):
        if j % 2 == 1:
            if j - 1 > 0:
                tree[j // 2] = tree[j] + tree[j - 1]
        else:
            if j + 1 <= N:
                tree[j // 2] = tree[j] + tree[j + 1]
            else:
                tree[j // 2] = tree[j]
    
    print("#{} {}".format(test_case, tree[L]))