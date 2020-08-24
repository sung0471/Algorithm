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

    return answer