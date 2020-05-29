import sys
sys.stdin = open('1248.txt')
import collections

def size(start):
    deq = collections.deque()
    deq.append(start)
    cnt = 0
    while deq:
        pos_n = deq.popleft()
        cnt += 1
        for i in parent.keys():
            if parent[i] == pos_n:
                if i == parent[i]:
                    continue
                deq.append(i)
    return cnt

def common(n1_list, n2_list):

    for n1 in n1_list:
        for n2 in n2_list:
            if n1 == n2:
                return n1
 

def ancestor(n):
    ancestor_list = [n]

    while n != 1:
        n = parent[n]
        ancestor_list.append(n)
    return ancestor_list

T = int(input())
for test_case in range(1, T + 1):
    V, E, n1, n2 = map(int, input().split())

    parent = {i: i for i in range(V + 1)}

    temp = list(map(int, input().split()))

    for i in range(0, E * 2, 2):
        parent[temp[i + 1]] = temp[i]
    common_ancestor = common(ancestor(n1), ancestor(n2))
    result = size(common_ancestor)


    print('#{} {} {}'.format(test_case, common_ancestor, result))


