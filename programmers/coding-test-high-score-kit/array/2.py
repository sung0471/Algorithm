# 가장 큰 수

from functools import cmp_to_key    # cmp를 사용하기 위한 함수
def solution(numbers):
    str_num = list(map(str, numbers))   # 모든 수를 str로 casting
    str_num = sorted(str_num, key=cmp_to_key(func))  # 두 수를 합칠 때, 커지는 순으로 정렬
    answer = ''.join(str_num)   # 하나로 합침
    return str(int(answer))


def func(x, y):
    if int(x+y) < int(y+x):     # 뒷 수가 더 크면
        return 1    # swap
    else:
        return -1