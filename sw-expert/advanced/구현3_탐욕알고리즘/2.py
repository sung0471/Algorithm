TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    dock_list = [list(map(int, input().split())) for _ in range(n)]

    dock_list.sort(key=lambda x: x[1])

    result = []
    visit = [0] * n
    result.append(dock_list[0])
    visit[0] = 1

    while True:
        # 겹치는 dock 제거
        for i in range(n):
            if result[-1][-1] > dock_list[i][0]:
                visit[i] = 1

        if 0 not in visit:
            break

        idx = 0
        value = 25
        for i in range(n):
            if visit[i] == 0 and result[-1][-1] <= dock_list[i][0] and dock_list[i][1] < value:
                idx = i
                value = dock_list[i][0]

        result.append(dock_list[idx])

    print('#{} {}'.format(test_case, len(result)))
