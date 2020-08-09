T = int(input())    # 테스트 케이스 개수 입력받음

for test_case in range(1, T+1):
    n, m = list(map(int, input().split()))  # 배열의 길이(n), 구간의 길이(m)을 입력받음
    num_list = list(map(int, input().split()))  # 검사할 배열을 입력받고, int로 변환

    max_v, min_v = sum(num_list[:m]), sum(num_list[:m])     # 초기값을 지정(배열의 0번째~m-1번째 구간합으로)

    for i in range(1, n-m+1):   # i를  1 ~ n-m까지 순회
        curr_sum = sum(num_list[i:i+m])     # 현재위치에서 m개의 구간만큼 합을 구함
        max_v = max(max_v, curr_sum)    # 최댓값을 계산하여 저장
        min_v = min(min_v, curr_sum)    # 최솟값을 계산하여 저장

    print(f'#{test_case} {max_v - min_v}')
