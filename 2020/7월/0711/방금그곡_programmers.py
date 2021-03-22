def solution(m, musicinfos):
    answer = '(None)'
    max_time = float('-inf')
    for string in musicinfos:

        temp_list = string.split(',')
        start, end, name, melody  = temp_list

        start = start.split(':')
        end = end.split(':')
        start = int(start[0]) * 60 + int(start[1])
        end = int(end[0]) * 60 + int(end[1])
        time = end - start

        melody_list = []
        for i in range(len(melody) - 1):
            if melody[i] == '#':
                continue

            if melody[i + 1] != '#':
                melody_list.append(melody[i])
            else:
                melody_list.append((melody[i] + melody[i + 1]))

        if melody[-1] != '#':
            melody_list.append(melody[-1])

        m_list = []
        for i in range(len(m) - 1):
            if m[i] == '#':
                continue

            if m[i + 1] != '#':
                m_list.append(m[i])
            else:
                m_list.append((m[i] + m[i + 1]))

        if m[-1] != '#':
            m_list.append(m[-1])

        melody_list = melody_list *  (time // len(melody_list)) + melody_list[:(time % len(melody_list))]

        is_true = False
        len_i = len(melody_list)
        len_j = len(m_list)
        i = 0
        j = 0

        while i < len_i:

            if melody_list[i] == m_list[j]:
                i += 1
                j += 1
                if j == len_j:
                    is_true = True
                    break
            else:
                i += (1 - j)
                j = 0
        if not is_true:
            continue
        if max_time < time:
            max_time = time
            answer = name

    return answer