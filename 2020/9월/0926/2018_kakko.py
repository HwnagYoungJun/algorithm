import requests
import json
from pprint import pprint


url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    return requests.get(uri, headers={'X-Auth-Token': token}).json()


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()


def simulator():
    user = 'tester'
    problem = 2
    count = 1

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))


    # 1. 일단 다 받는다.
    call_dict = {i: [] for i in range(1, 26)}
    len_call = 0

    pprint(oncalls(token))
    while len_call < 500:
    # 1-1. 다 받기 전에는 멈춰있는다.
        cmds = [{'elevator_id': 0, 'command': 'STOP'}]
        action(token, cmds)
        resp = oncalls(token)
        len_call = len(resp['calls'])

    resp = oncalls(token)
    for call in resp['calls']:
        call_start = call['start']
        call_end = call['end']
        call_id = call['id']
        call_dict[call_start].append((call_id, call_end))
    
    is_end = False
    status = "go_to_top"
    exit_dict = {i: [] for i in range(1, 26)}
    # 2. 오르락 내리락 한다.
    while not is_end:
        # resp = oncalls(token)
        # print(len(resp['calls']))
        # print(re)
        # 3. 오르락
        if status == 'go_to_top':
            for i in range(1, 26):
                print(f'this floor is {i}')
            #     resp = oncalls(token)
            #     for call in resp['calls']:
            #         call_start = call['start']
            #         call_end = call['end']
            #         call_id = call['id']
            #         if (call_id, call_end) not in call_dict[call_start]:
            #             call_dict[call_start].append((call_id, call_end))
                # pprint(oncalls(token))
                # 4. 만약 탈 사람이나 내릴 사람이 없으면 안한다.
                
                if call_dict[i] or exit_dict[i]:
                    
                    # 5. 멈춘다.
                    cmds = [{'elevator_id': 0, 'command': 'STOP'}]
                    action(token, cmds)
                    # 6. 연다
                    cmds = [{'elevator_id': 0, 'command': 'OPEN'}]
                    action(token, cmds)

                    # 7. 내릴사람을 내리게 해준다.
                    if exit_dict[i]:
                        exit_list = exit_dict[i]
                        # print(exit_dict)
                        cmds = [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': exit_list}]
                        action(token, cmds)
                    
                        exit_dict[i].clear()
                    
                    # 8. 탈 사람을 타게 해준다. 
                    # 8-1. 하지만 가득차버렸다면 탈 수가 없다 ㅠㅠ.
                    resp = oncalls(token)
                    is_full = len(resp['elevators'][0]['passengers'])
                    if call_dict[i] and is_full < 8:
                        enter_list = []
                        for_remove = []
                        for this_call in call_dict[i]:
                            enter_id = this_call[0]
                            enter_end = this_call[1]
                            resp = oncalls(token)
                            
                            temp = resp['elevators'][0]['passengers']
                            len_temp = len(temp)
                            enter_list.append(enter_id)
                            for_remove.append(this_call)
                            exit_dict[enter_end].append(enter_id)
                            if len(enter_list) + len_temp >= 8:
                                break

                        for m in for_remove:
                            call_dict[i].remove(m)
                        
                        # pprint(oncalls(token))
                        # print(enter_list)
                        cmds = [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': enter_list}]
                        action(token, cmds)


                    # 9. 닫는다.
                    cmds = [{'elevator_id': 0, 'command': 'CLOSE'}]
                    action(token, cmds)

                # 10. 최상층을 제외하고는 올라간다.
                if i != 25:
                    cmds = [{'elevator_id': 0, 'command': 'UP'}]
                    action(token, cmds)
                else:
                    cmds = [{'elevator_id': 0, 'command': 'STOP'}]
                    action(token, cmds)
            
            # 11. 상태를 다운으로 바꾼다.
            status = 'go_to_down'
            
        # 12. 내려간다. 
        elif status == 'go_to_down':
            for i in range(25, 0, -1):
                print(f'this floor is {i}')
                # 4. 만약 탈 사람이나 내릴 사람이 없으면 안한다.
                # for call in resp['calls']:
                #     call_start = call['start']
                #     call_end = call['end']
                #     call_id = call['id']
                #     if (call_id, call_end) not in call_dict[call_start]:
                #         call_dict[call_start].append((call_id, call_end))
                if call_dict[i] or exit_dict[i]:
                    
                    # 5. 멈춘다.
                    cmds = [{'elevator_id': 0, 'command': 'STOP'}]
                    action(token, cmds)

                    # 6. 연다
                    cmds = [{'elevator_id': 0, 'command': 'OPEN'}]
                    action(token, cmds)

                    # 7. 내릴사람을 내리게 해준다.
                    if exit_dict[i]:
                        exit_list = exit_dict[i]
                        cmds = [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': exit_list}]
                        action(token, cmds)
                    exit_dict[i].clear()
      
                    # 8. 탈 사람을 타게 해준다. 
                    # 8-1. 하지만 가득차버렸다면 탈 수가 없다 ㅠㅠ.
                    resp = oncalls(token)
                    is_full = len(resp['elevators'][0]['passengers'])
                    if call_dict[i] and is_full < 8:
                        enter_list = []
                        for_remove = []
                        for this_call in call_dict[i]:
                            enter_id = this_call[0]
                            enter_end = this_call[1]
                            resp = oncalls(token)
                            
                            temp = resp['elevators'][0]['passengers']
                            len_temp = len(temp)
                            enter_list.append(enter_id)
                            for_remove.append(this_call)
                            exit_dict[enter_end].append(enter_id)
                            if len(enter_list) + len_temp >= 8:
                                break
                        
                        for m in for_remove:
                            call_dict[i].remove(m)
                        
                        cmds = [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': enter_list}]
                        action(token, cmds)

                    # 9. 닫는다.
                    cmds = [{'elevator_id': 0, 'command': 'CLOSE'}]
                    action(token, cmds)

                # 10. 최상층을 제외하고는 올라간다.
                if i != 1:
                    cmds = [{'elevator_id': 0, 'command': 'DOWN'}]
                    action(token, cmds)
                else:
                    cmds = [{'elevator_id': 0, 'command': 'STOP'}]
                    action(token, cmds)

            # 11. 상태를 다운으로 바꾼다.
            status = 'go_to_top'
    
        resp = oncalls(token)
        is_end = resp['is_end']
    
    pprint(oncalls(token))


simulator()