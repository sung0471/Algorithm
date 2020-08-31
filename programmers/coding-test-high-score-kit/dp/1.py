# N으로 표현

def solution(N, number):
    answer = 0

    dp = [0] * (number+1)
    reserve = {}
    for i in range(5):
        reserve[i+1] = 2+i
        reserve[N * (i+1)] = 1+i

    for i in range(1, number+1):
        if i in reserve:
            dp[i] = reserve[i]
        else:
            pass

    return answer if answer <= 8 else -1


a = solution(5, 12)
print(a)

# 상원님
# def func(y, N):
#     y = str(y)
#     N = str(N)
#     for x in y:
#         if x != N: return False
#     return True
#
#
# def solution(N, number):
#     answer = 0
#
#     cont = []
#     part = []
#     check = set()
#
#     cont.append([0, N])
#
#     for idx in range(1, 9):
#
#         for x, y in cont:
#
#             if x == number: return idx
#             if (x, y) in check: continue
#             check.add((x, y))
#
#             # 요기
#             cont.append([x + y, 0])
#             cont.append([x - y, 0])
#             cont.append([x * y, 0])
#             if (y != 0): cont.append([x // y, 0])
#         # 요기
#
#         part.append([x, y + N])
#         part.append([x, y - N])
#         part.append([x, y * N])
#         part.append([x, y // N])
#
#         if func(y, N): part.append([x, y * 10 + N])
#
#     cont = part[:]
#
#
# return -1