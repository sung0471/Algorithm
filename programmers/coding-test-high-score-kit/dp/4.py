# 도둑질
# dfs : 시간초과

def dfs(money, visit, curr, length):
    score = money[curr]
    for variance in [-1, 0, 1]:
        pos = curr + variance
        visit[pos % length] = True
    # print(visit, score)
    temp = 0
    for i in range(length):
        if not visit[i]:
            score_ = dfs(money, visit[:], i, length)
            if temp < score_:
                temp = score_
    score += temp

    return score


def solution(money):
    length = len(money)
    answer = 0
    for i in range(length):
        # print(i)
        visit = [False] * length
        score = dfs(money, visit[:], i, length)
        if score > answer:
            answer = score
        # print(score)

    return answer


# dp
# https://doohong.github.io/2019/03/14/Algorithm-%20thievery/

def solution(money):
    length = len(money)

    dp_first = [0] * length     # i=0을 선택하는 경우
    dp_second = [0] * length    # i=1을 선택하는 경우
    dp_first[:2] = [money[0]] * 2   # i=0이면, money[0]으로 2개 채움
    dp_second[1] = money[1]         # i=1이면, money[1]으로 dp[1]만 채움
    for i in range(2, length):  # i=2 ~ length-1
        if i != length - 1:     # 마지막 index 전까지는
            # i-1의 최대값 vs i-2의 최대값 + 현재 도둑질한 값 중 최대값
            dp_first[i] = max(dp_first[i - 1], dp_first[i - 2] + money[i])
        else:
            # 마지막 집은 털 수 없으므로, i-1의 값을 그대로 복사
            dp_first[i] = dp_first[i - 1]
        
        # second는 마지막 집을 털 수 있으므로 처음부터 끝까지 진행
        dp_second[i] = max(dp_second[i - 1], dp_second[i - 2] + money[i])
    
    # 첫 번째를 고른 경우 vs 두 번째를 고른 경우 중 최댓값
    answer = max(dp_first[-1], dp_second[-1])
    return answer


a = solution([1, 2, 3, 1])
print(a)
