# h-index

def solution(citations):
    h_index = max(citations)    # 인용수의 최댓값 저장

    while True:
        count = 0
        for cite in citations:  # 모든 인용수 반복
            if cite >= h_index: # h_index보다 큰 인용수인 논문 수 저장
                count += 1
        if count >= h_index:    # h보다 큰 인용논문 수가 h 이상이면 끝
            break
        h_index -= 1    # 아니면, h -= 1하면서 반복

    return h_index


a = solution([3, 0, 6, 1, 5])
print(a)