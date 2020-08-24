# 소수 찾기

def solution(numbers):
    import itertools    # 조합을 위한 라이브러리
    import math

    answer = 0  # 소수 개수 저장할 변수
    combination_list = []   # 숫자 조합을 저장할 리스트
    number = [n for n in numbers]   # string 숫자를 배열로 저장
    print(number)

    for i in range(1, len(number) + 1):     # 배열 길이 n만큼 숫자 조합 구하기
        combination_list += list(map(int, map(''.join, itertools.permutations(number, i))))
    combination_list = set(combination_list)    # 중복되는 수 제거

    print(combination_list)
    for num in combination_list:    # 모든 조합 수 순회
        if num != 1:    # 1은 소수가 아니라 제외
            check_prime = 0
            # 1 ~ sqrt(num) 까지 순회
            for i in range(1, int(math.sqrt(num))+1):
                if num % i == 0:    # 약수면 +1
                    check_prime += 1
            if check_prime == 1:    # 약수의 개수가 1이면, 소수
                answer += 1

    return answer

a = solution("17")
print(a)

# 다른 사람 풀이 중에 set을 이용한 풀이
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)
