import sys
sys.stdin = open('추석트래픽.txt')


def solution(lines):
    time_dict = dict()
    computer = -1
    for line in lines:
        computer += 1
        end_time, time = trans(line)
        if computer == 0:
            start_time = end_time - time + 1
        
        if computer == len(lines) - 1:
            real_end = end_time
        for i in range(end_time, end_time - time, -1):
            if time_dict.get(i) == None:
                time_dict[i] = [computer]
            
            else:
                time_dict[i].append(computer)
                
    answer = 1
    for i in range(start_time, real_end + 1):
        print(i)
        temp_set = set()
        for j in range(i, i + 1000):
            if time_dict.get(j) == None:
                continue
            
            for k in time_dict[j]:
                temp_set.add(k)
        answer = max(answer, len(temp_set))

    return answer

def trans(line):

    def T_to_ms(S):
        res = 0
        res += int(S[0:2]) * 3600000
        res += int(S[3:5]) * 60000
        res += int(S[6:8]) * 1000
        res += int(S[9:12])
        return res

    temp = list(line.split())
    S = temp[1]
    end_time = T_to_ms(S)

    T = temp[2][0:-1]

    if len(T) != 1:
        s_ms = T.split('.')
        s = int(s_ms[0]) * 1000
        if len(s_ms[1]) == 1:
            ms = s_ms[1] +'00'
        elif len(s_ms) == 2:
            ms = s_ms[1] + '0'
        ms = int(ms)
        time = s + ms

    else:
        time = int(T) * 1000

    return (end_time, time)
    

lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

print(solution(lines))