def solution(records):
    answer = []
    temps = []
    name_dict = dict()
    for record in records:

        record = list(record.split())
        
        if record[0] != 'Leave':
            command = record[0]
            ID = record[1]
            nick_name = record[2]

        else:
            command = record[0]
            ID = record[1]    

        if command == 'Enter':
            temps.append([ID, '님이 들어왔습니다.'])
            enroll(ID, name_dict, nick_name)
            
        elif command == 'Leave':
            temps.append([ID, '님이 나갔습니다.'])
        
        else:
            enroll(ID, name_dict, nick_name)    
    
    for temp in temps:
        n, s = temp
        answer.append(f'{name_dict[n]}{s}')
        
    return answer

def enroll(name, d, nick_name):
    
    d[name] = nick_name
    
    return


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))