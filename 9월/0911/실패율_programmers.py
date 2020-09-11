def solution(N, stages):
    num_survivor = len(stages)
    stages_dict = {stage: 0 for stage in range(1, N + 1)}
    pq = []
    result = []

    for stage in stages:

        if stage == N + 1:
            continue
        
        stages_dict[stage] += 1
        
    for stage_key, stage_value in stages_dict.items():
        
        if num_survivor == 0:
            fail = 0
        else:
            fail = stage_value / num_survivor
            num_survivor -= stage_value
        
        pq.append((fail, stage_key))
    
    pq.sort(key=lambda x: (-x[0], x[1]))
    
    for i in pq:
        result.append(i[1])
    print(result)
    return result