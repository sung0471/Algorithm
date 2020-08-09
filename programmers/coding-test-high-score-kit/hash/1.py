# 해시/완주하지 못한 선수

def solution(participant, completion):
    temp_dict = dict()
    for name in participant:
        if name not in temp_dict:
            temp_dict[name] = 1
        else:
            temp_dict[name] += 1

    for name in completion:
        if name in temp_dict:
            temp_dict[name] -= 1
            if temp_dict[name] == 0:
                temp_dict.pop(name)
    return list(temp_dict.keys())[0]
