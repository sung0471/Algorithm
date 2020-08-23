# 더맵게

def solution(scoville, K):
    import heapq
    answer = 0

    # scoville를 heap 자료구조로 저장
    heapq.heapify(scoville)

    # 큐 길이가 최소 2이면서, 최솟값이 K보다 작으면 반복
    while len(scoville) > 1 and scoville[0] < K:
        a, b = heapq.heappop(scoville), heapq.heappop(scoville)     # 가장 작은 수 2개 pop
        c = a + 2 * b       # 두 음식을 섞음
        scoville.append(c)  # 큐에 삽입 (이 때, 재정렬됨)
        answer += 1     # 섞은 수 +1
    # 큐 길이가 1이거나, 최솟값이 K 이상이면 끝남

    # 남은 1개 원소가 K보다 작으면 실패
    if len(scoville) == 1 and scoville[0] < K:
        answer = -1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))

