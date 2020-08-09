# 해시/위장

def solution(clothes):
    dict_list = dict()
    for value, key in clothes:
        if key not in dict_list:
            dict_list[key] = 1
        else:
            dict_list[key] += 1

    answer = 1
    for value in dict_list.values():
        answer *= value + 1

    return answer - 1
