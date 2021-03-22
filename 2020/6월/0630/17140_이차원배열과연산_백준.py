import sys
sys.stdin = open('17140.txt')

def rotate_90(r, c, g):

    ret = [[0 for _ in range(r)] for _ in range(c)]
    for row in range(r):
        for col in range(c):
            ret[col][row] = g[row][col]

    return ret[:]

r, c, K = map(int, input().split())
r -= 1
c -= 1
init_list = [list(map(int, input().split())) for _ in range(3)]

R = 3
C = 3
next_list = init_list[:]
mode = 'R'
time = 0
while time < 101:
    map_list = next_list[:]
    if R > r and C > c:
        if map_list[r][c] == K:
            break
    time += 1
    next_list = []
    max_length = float('-inf')
    if mode == 'R':
        for row in range(R):
            num_dict = dict()
            temp_list = []
            index = 0
            for col in range(C):
                target = map_list[row][col]
                if target == 0:
                    continue
                if num_dict.get(target) == None:
                    temp_list.append([target, 1])
                    num_dict[target] = index
                    index += 1
                else:
                    temp_list[num_dict[target]][1] += 1
            
            temp_list.sort(key=lambda x: (x[1], x[0]))
            if len(temp_list) > 100:
                temp_list[:100]
            max_length = max(max_length, 2 * len(temp_list))
            pre_list = []
            
            for i in temp_list:
                for j in i:
                    pre_list.append(j)
            
            next_list.append(pre_list)
        
        for row in range(R):
            if len(next_list[row]) < max_length:
                for i in range(max_length - len(next_list[row])):
                    next_list[row].append(0)
        R = R
        C = max_length

    else:
        for col in range(C):
            num_dict = dict()
            temp_list = []
            index = 0
            for row in range(R):
                target = map_list[row][col]
                if target == 0:
                    continue
                if num_dict.get(target) == None:
                    temp_list.append([target, 1])
                    num_dict[target] = index
                    index += 1
                else:
                    temp_list[num_dict[target]][1] += 1
            
            temp_list.sort(key=lambda x: (x[1], x[0]))
            if len(temp_list) > 100:
                temp_list[:100]
            max_length = max(max_length, 2 * len(temp_list))
            pre_list = []
            
            for i in temp_list:
                for j in i:
                    pre_list.append(j)
            
            next_list.append(pre_list)
        
        for row in range(C):
            if len(next_list[row]) < max_length:
                for i in range(max_length - len(next_list[row])):
                    next_list[row].append(0)

        # for i in next_list:
        #     print(*i)
        # print()
        next_list = rotate_90(C, max_length, next_list)
        # for i in next_list:
        #     print(*i)
        # print()

        R = max_length
        C = C


    
    if R >= C:
        mode = 'R'
    else:
        mode = 'C'

if time == 101:
    print(-1)
else:
    print(time)
