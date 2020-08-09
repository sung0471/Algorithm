# 스택/큐 / 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_num = len(truck_weights)
    truck_time = list()

    finish_truck = list()
    bridge_truck = list()
    while len(finish_truck) < truck_num:
        answer += 1

        for i in range(len(truck_time)):
            truck_time[i] += 1

        if len(truck_time) > 0 and truck_time[0] == bridge_length:
            finish_truck.append(bridge_truck.pop(0))
            truck_time.pop(0)

        bridge_weight = sum(bridge_truck)
        if len(truck_weights) > 0 and weight >= bridge_weight + truck_weights[0]:
            temp_truck = truck_weights.pop(0)
            bridge_truck.append(temp_truck)
            truck_time += [0]

    return answer
