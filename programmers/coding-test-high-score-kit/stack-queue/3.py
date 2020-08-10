# 스택/큐 / 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_num = len(truck_weights)  # 트럭 개수
    truck_time = list()     # 트럭이 다리에 잔류한 시간

    finish_truck = list()   # 다리를 다 건넌 트럭의 weight를 저장하는 변수
    bridge_truck = list()   # 다리 위에 있는 트럭을 저장하는 변수
    while len(finish_truck) < truck_num:    # 트럭이 아직 다 안 건넜으면
        answer += 1

        for i in range(len(truck_time)):    # 다리 위에 있는 트럭들을 1초씩 이동
            truck_time[i] += 1

        if len(truck_time) > 0 and truck_time[0] == bridge_length:  # 이미 다리 끝에 도달한 트럭은
            finish_truck.append(bridge_truck.pop(0))    # 다리에서 빼서 목적지로 이동
            truck_time.pop(0)   # 트럭의 잔류시간 변수에서 제거

        bridge_weight = sum(bridge_truck)       # 다리 위에 있는 트럭들의 무게
        if len(truck_weights) > 0 and weight >= bridge_weight + truck_weights[0]:   # 다리 위로 트럭이 들어올 수 있으면
            temp_truck = truck_weights.pop(0)   # 대기 중인 트럭 하나를 빼서
            bridge_truck.append(temp_truck)     # 다리 위로 옮김
            truck_time += [0]       # 트럭의 잔류시간 변수에 하나 추가

    # 트럭이 다 건넜으면 clear
    return answer

# 상원님
# 새로운 트럭이 들어올때, 나가야될 트럭을 내보내는 방식
# max로 현재 시간과 (입장시간 + 통과시간) 비교하는게 핵심
# 민기님
# Queue로 해결

# 시점을 껑충껑충 뛰는 방법이 더 좋음
