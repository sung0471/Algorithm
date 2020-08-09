# 스택/큐 / 기능개발

def solution(progresses, speeds):
    times_list = list()
    answer = []
    for progress, speed in zip(progresses, speeds):
        times = (100 - progress) // speed
        times += 1 if (100 - progress) % speed > 0 else 0
        times_list.append(times)

    day = 0
    process_num = 0
    for time in times_list:
        if day < time:
            answer.append(process_num)
            day = time
            process_num = 1
        else:
            process_num += 1

    answer.append(process_num)

    return answer[1:]
