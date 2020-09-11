import math

def solution(str1, str2):
    len_union = 0
    len_intersection = 0
    len_str1 = len(str1)
    len_str2 = len(str2)
    str1_dict = dict()
    str2_dict = dict()
    cnt1 = 0
    cnt2 = 0
    for i in range(len_str1 - 1):
        first = str1[i]
        second = str1[i + 1]
        
        if (not first.isalpha() or not second.isalpha()):
            continue

        if first.isalpha() == True:
            first = first.upper()
        
        if second.isalpha() == True:
            second = second.upper()

        word = first + second
        if str1_dict.get(word) == None:
            str1_dict[word] = 1
        else:
            str1_dict[word] += 1
        cnt1 += 1


    for i in range(len_str2 - 1):
        first = str2[i]
        second = str2[i + 1]
                
        if (not first.isalpha() or not second.isalpha()):
            continue

        if first.isalpha() == True:
            first = first.upper()
        if second.isalpha() == True:
            second = second.upper()

        word = first + second
        if str2_dict.get(word) == None:
            str2_dict[word] = 1
        else:
            str2_dict[word] += 1
        
        cnt2 += 1
    for word, banbuks in str2_dict.items():
        
        for banbuk in range(banbuks):
            if str1_dict.get(word) != None:
                len_intersection += 1
                if str1_dict[word] == 1:
                    del str1_dict[word]

                else:
                    str1_dict[word] -= 1
    
    len_union = cnt1 + cnt2 - len_intersection
    if cnt1 + cnt2  == 0:
        return 65536
    answer = math.floor((len_intersection / len_union) * 65536)
    return answer

# 1. 2글자씩 나눈다. 이때, 대문자로 전부 바꿔준다
# 2. 딕셔너리로 방을 만들고 한개당 1을준다
# 3. 2번째에는 해쉬값으로 그친구가 있으면 같은게 있는거다