import collections

def solution(bridge_length, weight, truck_weights):
    time = 0
    passing_truck = collections.deque()
    wating_truck = collections.deque()
    for i in truck_weights:
        wating_truck.append(i)
    temp = 0
    while True:
        
        if passing_truck:
            if time == passing_truck[0][1]:
                temp -= passing_truck[0][0]
                passing_truck.popleft()
            
        if wating_truck:
            if temp + wating_truck[0] <= weight:
                a = wating_truck.popleft()
                passing_truck.append((a, time + bridge_length))
                temp += a
            
        if not passing_truck and not wating_truck:
            break

        time += 1

    return time + 1