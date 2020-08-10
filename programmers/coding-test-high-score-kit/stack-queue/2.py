# 스택/큐 / 기능개발

def solution(progresses, speeds):
    times_list = list()
    answer = []
    for progress, speed in zip(progresses, speeds):     # progress 배열, speed 배열을 순회
        times = (100 - progress) // speed       # 작업 완료 일자를 계산 (몫)
        times += 1 if (100 - progress) % speed > 0 else 0   # 작업 완료 시간이 남으면 하루 +1
        times_list.append(times)

    day = 0     # 작업 완료일
    process_num = 0     # 처리횟수
    for time in times_list:
        if day < time:      # 이전 작업 완료일자 < 현재 작업 완료일자
            answer.append(process_num)  # 이전까지 작업한 개수 저장
            day = time
            process_num = 1     # 작업한 개수 1로 초기화
        else:               # 작업 완료일자가 다음 작업완료일자보다 크면
            process_num += 1    # 작업한 개수 +1

    answer.append(process_num)  # 마지막 작업이 끝나고 저장하지 않은 작업한 개수를 저장

    return answer[1:]       # 초기값으로 저장된 0을 예외처리

# 건우님
# 하루마다 progress를 speed씩 올리면서 처리하도록 함

# 민기님, 상원님
# progress 반복 돌면서, day를 계산해서 해결함
