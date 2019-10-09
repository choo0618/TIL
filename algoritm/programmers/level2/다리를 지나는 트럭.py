def solution(bridge_length, weight, truck_weights):
    Time = 0
    L = len(truck_weights)
    bridge = [0] * (bridge_length + 1)
    Arr = []
    while True:
        if bridge[-1]:
            Arr.append(bridge[-1])
            bridge[-1]=0
        if len(Arr)==L:break
        if truck_weights and sum(bridge)+truck_weights[0] <= weight:
            bridge[0] = truck_weights.pop(0)
        bridge.insert(bridge.pop(),0)
        Time += 1
    return Time+1
