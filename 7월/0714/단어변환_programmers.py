import collections


def solution(begin, target, words):
    answer = 0
    
    if target in words:
        answer = bfs(begin, target, words)
    
    return answer


def change(s1, s2, len_s):
    cnt = 0
    for i in range(len_s):
        if s1[i] != s2[i]:
            cnt += 1
        
        if cnt > 1:
            break
            
    if cnt == 1:
        return True
    else:
        return False
    
    
def bfs(begin, target, words):
    len_w = len(words)
    deq = collections.deque()
    deq.append((begin, 0))
    visit = [0 for _ in range(len_w)]
    while deq:
        string, cnt = deq.popleft()
        for w in range(len_w):
            
            if visit[w] == 1:
                continue
            
            if not change(string, words[w], len(begin)):
                continue
            
            if words[w] == target:
                return cnt + 1
            
            visit[w] = 1
            deq.append((words[w], cnt + 1))
            
    return 0