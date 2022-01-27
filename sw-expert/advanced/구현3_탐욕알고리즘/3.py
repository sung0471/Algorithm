T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    card_l = list(map(int, input().split()))
    card_num = []
    for _ in range(2):
        card_num.append([0 for i in range(10)])
    result = -1

    # print('{} : {}, {}'.format(test_case, card_l[::2], card_l[1::2]))

    for i, num in enumerate(card_l):
        player = 0 if i % 2 == 0 else 1

        # 하나의 숫자가 3번나오면 끝내기
        card_num[player][num] += 1
        if card_num[player][num] == 3:
            result = player
            break

        # 연속된 숫자가 3개 이상인지 판단하기
        if num < 8 and card_num[player][num] and card_num[player][num + 1] and card_num[player][num + 2]:
            result = player
            break
        if 0 < num < 9 and card_num[player][num - 1] and card_num[player][num] and card_num[player][num + 1]:
            result = player
            break
        if 1 < num and card_num[player][num - 2] and card_num[player][num - 1] and card_num[player][num]:
            result = player
            break

    print('#{} {}'.format(test_case, result + 1))
