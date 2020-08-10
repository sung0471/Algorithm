# 해시/위장

def solution(clothes):
    dict_list = dict()
    for value, key in clothes:  # key: [value]로 저장
        if key not in dict_list:
            dict_list[key] = 1
        else:
            dict_list[key] += 1

    answer = 1
    for value in dict_list.values():    # 경우의 수 계산
        answer *= value + 1

    return answer - 1   # 모두 입지 않은 경우의 수 빼기

# 건우님
