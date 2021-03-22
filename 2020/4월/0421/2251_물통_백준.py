import sys
sys.stdin = open('2251.txt')
import collections

def bfs():
    deq = collections.deque()
    deq.append((c, b, a))
    possible = set()
    possible.add((c, b, a))

    while deq:
        cc, bb, aa = deq.popleft()
        if cc != 0:
            for w in range(2):
                if w == 0: # C에서 B로 물을 붓는다
                    if bb < B:
                        if B > bb + cc:
                            if (0, bb + cc, aa) not in possible:
                                possible.add((0, bb + cc, aa))
                                deq.append((0, bb + cc, aa))
                                # print((0, bb + cc, aa), 'a')
            
                        else:
                            if (cc + bb - B, B, aa) not in possible:
                                possible.add((cc + bb - B, B, aa))
                                deq.append((cc + bb - B, B, aa))
                                # print((cc + bb - B, B, aa))


                else: # C에서 A로 물을 붓는다.
                    if aa < A:
                        if A > aa + cc:
                            if (0, bb, aa + cc) not in possible:
                                possible.add((0, bb, aa + cc))
                                deq.append((0, bb, aa + cc))
                        else:
                            if (cc + aa - A, bb, A) not in possible:
                                possible.add((cc + aa - A, bb, A))
                                deq.append((cc + aa - A, bb, A))
                                # print((cc + aa - A, bb, A))
        if bb != 0: 
            for w in range(2):
                if w == 0: # B에서 A로 물을 붓는다
                    if aa < A :
                        if A > aa + bb:
                            if (cc, 0, aa + bb) not in possible:
                                possible.add((cc, 0, aa + bb))
                                deq.append((cc, 0, aa + bb))
                        else:
                            if (cc, bb + aa - A, A) not in possible:
                                possible.add((cc, bb + aa - A, A))
                                deq.append((cc, bb + aa - A, A))
                                # print((cc, bb + aa - A, A))

                else: # B에서 C로 물을 붓는다.
                    if cc < C:
                        if C > bb + cc:
                            if (bb + cc, 0, aa) not in possible:
                                possible.add((bb + cc, 0, aa))
                                deq.append((bb + cc, 0, aa))
                        else:
                            if (C, bb + cc - C, aa) not in possible:
                                possible.add((C, bb + cc - C, aa))
                                deq.append((C, bb + cc - C, aa))
                                # print((C, bb + cc - C, aa))

        if aa != 0:
            for w in range(2):
                if w == 0: # A에서 B로 불을 붓는다
                    if bb < B:
                        if B > aa + bb:
                            if (cc, aa + bb, 0) not in possible:
                                possible.add((cc, aa + bb, 0))
                                deq.append((cc, aa + bb, 0))
                        else:
                            if (cc, B, aa + bb - B) not in possible:
                                possible.add((cc, B, aa + bb - B))
                                deq.append((cc, B, aa + bb - B))


                else: # A에서 C로 물을 붓는다.
                    if cc < C:
                        if C > aa + cc:
                            if (aa + cc, bb, 0) not in possible:
                                possible.add((aa + cc, bb, 0))
                                deq.append((aa + cc, bb, 0))
                        else:
                            if (aa + cc - C, bb, C) not in possible:
                                possible.add((aa + cc - C, bb, C))
                                deq.append((aa + cc - C, bb, C))
    return possible


A, B, C = map(int, input().split())

a = 0
b = 0
c = C

temp_list = list()
for result in bfs():
    cccc, bbbb, aaaa = result
    if aaaa == 0:
        if cccc not in temp_list:
            temp_list.append(cccc)

temp_list.sort()
print(*temp_list)
