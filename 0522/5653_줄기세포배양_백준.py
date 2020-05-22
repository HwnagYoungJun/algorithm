dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

import sys
sys.stdin = open('5653.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    inactive_dict = dict()
    active_dict = dict()
    die_dict = dict()

    init_list = [list(map(int, input().split())) for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if init_list[row][col] == 0:
                continue
            inactive_dict[(row, col)] = [init_list[row][col], 0]

    for _ in range(K):
        # 비활성화
        delete_data = set()
        for key, value in inactive_dict.items():
            inactive_dict[key][1] += 1
            live_inact = value[0]
            time_inact = value[1]

            if live_inact == time_inact:
                delete_data.add((key, live_inact))
        # 활성화
        go_to_die = set()
        for key, value in active_dict.items():
            live = value[0]
            time = value[1]
            
            if time == 0:
                r, c = key
                for w in range(4):
                    nr = r + dr[w]
                    nc = c + dc[w]
                    nkey = (nr, nc)
                    if nkey in active_dict:
                        continue
                    if nkey not in die_dict:
                        if nkey in inactive_dict:
                            # 초기배양이 겹칠 떄
                            if inactive_dict[nkey][1] != 0:
                                continue
                            if live > inactive_dict[nkey][0]:
                                inactive_dict[nkey][0] = live
                            else:
                                pass                   
                        else:
                            inactive_dict[nkey] = [live, 0]

            active_dict[key][1] += 1
            if active_dict[key][0] == active_dict[key][1]:
                die_dict[key] = True
                go_to_die.add(key)
                    
        for delete in go_to_die:
            del active_dict[delete]

        for add_key, add_live in delete_data:
            active_dict[add_key] = [add_live, 0]
            del inactive_dict[add_key]

    cnt = 0
    for i in inactive_dict:
        cnt += 1
    for j in active_dict:
        cnt += 1
    
    print('#{} {}'.format(test_case, cnt))