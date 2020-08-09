# 스택/큐 / 프린터

def solution(priorities, location):
    answer = 0
    while True:
        if len(priorities) == 1:
            answer += 1
            break
        else:
            first = priorities[0]
            max_num = max(priorities[1:])
            if first >= max_num:
                answer += 1
                priorities.pop(0)
                if location == 0:
                    break
                else:
                    location -= 1
            else:
                priorities.append(priorities.pop(0))
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1

    return answer
