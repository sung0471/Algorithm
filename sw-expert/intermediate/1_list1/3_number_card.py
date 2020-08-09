T = int(input())    # 총 테스트 케이스 개수 입력받음

for test_case in range(1, T+1):
    card_count = int(input())   # 카드 개수를 입력받음
    cards = input()     # 카드들을 string으로 입력받음
    count_list = [0] * 10   # 카드위에 적힌 수가 등장한 횟수를 저장할 배열 생성
    max_count = 0       # 가장 많이 등장한 횟수를 저장할 변수

    for card in cards:  # 전체 카드를 순회
        card_num = int(card)    # 카드 번호는 string이므로 int로 변환
        count_list[card_num] += 1   # 카드 등장 횟수 +1
        max_count = max(max_count, count_list[card_num])    # 카드 등장 횟수가 최댓값일 경우 업데이트

    for i in range(9, -1, -1):  # 카드 번호 9~0까지 순회하면서 체크
        if count_list[i] == max_count:  # 카드 번호 등장 횟수가 최댓값이면,
            print(f'#{test_case} {i} {count_list[i]}')  # 카드 번호, 등장횟수를 출력후 종료
            break
