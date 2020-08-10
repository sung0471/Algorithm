# 스택/큐 / 주식가격

def solution(prices):
    answer = []
    for i in range(len(prices) - 1):    # 0 ~ len(prices)-2까지 순회
        count = 0       # 상승하는 시간을 저장하는 변수
        for j in range(i + 1, len(prices)):     # i+1 ~ len(prices)-1까지 순회
            if prices[i] <= prices[j]:  # 가격이 상승하거나 같으면
                count += 1  # 상승하는 시간 +1
            else:
                count += 1  # 상승하지 않지만, 감소하기 직전까지의 시간을 +1 해야함
                break       # 감소했으므로 종료
        answer += [count]   # 주식가격 하나의 상승시간을 저장

    answer += [0]   # 맨 마지막의 주식가격은 0이므로, 0으로 저장
    return answer
