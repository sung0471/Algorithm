# 타겟 넘버

def solution(numbers, target):
    queue = [numbers[0], -numbers[0]]
    answer = 0

    idx = 1
    number_length = len(numbers)
    while idx < number_length:
        next_queue = []
        number = numbers[idx]
        for num in queue:
            next_queue.append(num + number)
            next_queue.append(num - number)
        queue = next_queue[:]
        idx += 1
    for num in queue:
        if num == target:
            answer += 1

    return answer