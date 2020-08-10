# 스택/큐 / 프린터

def solution(priorities, location):
    answer = 0
    while True:
        if len(priorities) == 1:    # 프린터에 남은 개수가 1개면
            answer += 1     # 작업 개수 +1
            break           # 종료
        else:
            first = priorities[0]   # 맨 앞 작업의 중요도
            max_num = max(priorities[1:])   # 맨 앞 작업을 제외한 나머지 작업의 중요도 최댓값
            if first >= max_num:    # 맨 앞 작업의 중요도가 제일 크면
                answer += 1     # 작업 개수 +1
                priorities.pop(0)   # 작업 list에서 제거
                if location == 0:   # 검사하는 location이 현재 위치면 종료
                    break
                else:               # location > 0이면 -1
                    location -= 1
            else:                   # 다른 작업이 중요도가 더 크면
                priorities.append(priorities.pop(0))    # 앞의 작업을 맨 뒤로 이동
                if location == 0:   # location 위치가 0이었으면, 맨 뒤로 이동
                    location = len(priorities) - 1
                else:               # location > 0이면, -1
                    location -= 1

    # 작업 종료되면, 작업횟수 출력
    return answer

# 민기님
# sorted해서 max값부터 차례대로 정렬된 배열 선언
# Queue에 (index, value)를 요소로 삽입
