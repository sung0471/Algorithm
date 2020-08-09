T = int(input())    # Test case 개수 입력받음

for test_case in range(1, T+1):
    k, n, m = map(int, input().split())     # 버스 최대이동수(k), 정류장 개수(n), 충전기 설치 개수(m)을 입력받음
    charge_station = list(map(int, input().split()))    # 충전기가 설치된 위치를 배열로 입력받음
    curr = 0    # 버스가 이동한 위치를 저장하는 변수
    count = 0   # 버스가 충전한 횟수를 저장하는 변수

    while True:
        if curr + k >= n:       # 만약 정류장 끝에 도착하면 끝
            break
        check = False   # 충전했는지 여부를 체크하는 변수
        for i in range(m-1, -1, -1):    # 종점부터 탐색
            if curr < charge_station[i] <= curr + k:    # 현재 위치에서 갈 수 있는 위치인지 검사
                count += 1                  # 충전횟수 +1
                curr = charge_station[i]    # 버스 위치를 이동
                check = not check           # 충전했다고 체크
                break                       # 탐색을 중지
        if not check:   # 충전을 못했으면
            count = 0   # 충전 횟수=0으로 설정
            break       # 끝내기

    print(f'#{test_case} {count}')
