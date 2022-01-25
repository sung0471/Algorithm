T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight.sort(reverse=True)
    truck.sort(reverse=True)

    weight_i = 0
    truck_i = 0
    total = 0

    # print(weight)
    # print(truck)
    while weight_i < len(weight) and truck_i < len(truck):
        # print(weight_i, truck_i)
        if truck[truck_i] >= weight[weight_i]:
            total += weight[weight_i]
            truck_i += 1
            weight_i += 1
        else:
            weight_i += 1

    print('#{} {}'.format(test_case, total))
