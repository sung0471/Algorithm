T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lines = int(input())
    map_ = list()
    acc_map = list()
    for _ in range(lines):
        map_.append(list(map(int, input().split())))
        acc_map.append([0]*lines)

    acc_map[0][0] = map_[0][0]
    for i in range(lines):
        for j in range(lines):
            if i == 0 and j == 0:
                continue
            elif j == 0:
                acc_map[i][j] += acc_map[i-1][j] + map_[i][j]
            elif i == 0:
                acc_map[i][j] += acc_map[i][j-1] + map_[i][j]
            else:
                min_ = min(acc_map[i][j-1], acc_map[i-1][j])
                acc_map[i][j] += min_ + map_[i][j]

    print('#{} {}'.format(test_case, acc_map[-1][-1]))
