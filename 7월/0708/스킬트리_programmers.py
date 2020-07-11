from pprint import *

def solution(skill, skill_trees):
    
    answer = 0
    len_s = len(skill)
    preceding_dict = {i: [] for i in range(26)}
    
    for i in range(len(skill) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            # 'A' = 65
            ord_i = ord(skill[i]) - 65
            ord_j = ord(skill[j]) - 65
            preceding_dict[ord_i].append(ord_j)
    
    for skill_tree in skill_trees:
        
        temp = []
        fail = False
        
        for string in skill_tree:
            if fail:
                break
            ord_str = ord(string) - 65
            if not preceding_dict[ord_str]:
                temp.append(ord_str)
            else:
                for preceding_skill in preceding_dict[ord_str]:
                    if preceding_skill not in temp:
                        fail = True
                        break
                else:
                    temp.append(ord_str)
                
        if not fail:
            answer += 1
            
    return answer