from itertools import permutations
# https://ourcstory.tistory.com/414


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    map_ = list()
    for i in range(n):
        map_.append(list(map(int, input().split())))

    # permutations 으로 조합리스트 -> 리스트 캐스팅 -> 각 경우의 수마다 누적값 계산 -> 최솟값 출력
    all_pm = list(map(list, permutations([_ for _ in range(1, n)], n-1)))
    acc = [0] * len(all_pm)     # len = 조합 개수
    before_i = [0 for _ in range(len(all_pm))]
    for j in range(n-1):    # n-1 = 조합의 길이
        for i, list_ in enumerate(all_pm):
            next_i = list_[j]
            acc[i] += map_[before_i[i]][next_i]
            before_i[i] = next_i

    for i in range(len(all_pm)):
        acc[i] += map_[before_i[i]][0]

    print('#{} {}'.format(test_case, min(acc)))
