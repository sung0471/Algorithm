# K번째 수

def solution(array, commands):
    answer = []

    for command in commands:
        s, e, idx = command
        tmp = sorted(array[s-1:e])[idx-1]   # s-1~e 범위 slice, idx-1 위치 검색
        answer.append(tmp)

    return answer

a = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])

print(a)
