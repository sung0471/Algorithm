# 해시/완주하지 못한 선수

def solution(participant, completion):
    temp_dict = dict()
    for name in participant:    # dict()에 각 이름이 등장한 수를 추가
        if name not in temp_dict:
            temp_dict[name] = 1
        else:
            temp_dict[name] += 1

    for name in completion:     # 등장한 사람은 dict()에서 등장한 수를 감소
        if name in temp_dict:
            temp_dict[name] -= 1
            if temp_dict[name] == 0:
                temp_dict.pop(name)

    return list(temp_dict.keys())[0]    # 혼자 남은 사람의 이름을 return

#   from collections import Counter
#   Counter 객체 간의 +, -이 가능
