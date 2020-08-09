T = int(input())    # test_case 수 입력받음

for test_case in range(1, T + 1):
    n = int(input())    # 앞으로 입력받는 배열의 개수 N을 입력받음
    num_list = list(map(int, input().split()))  # min, max를 구할 숫자들의 배열을 입력받음
    max_v, min_v = 0, 1000001   # min, max 값을 저장할 변수의 초기값 지정
    for i in range(n):  # 배열을 전체 돌면서, min, max 값 계산
        max_v = max(max_v, num_list[i])
        min_v = min(min_v, num_list[i])

    print(f'#{test_case} {max_v - min_v}')
