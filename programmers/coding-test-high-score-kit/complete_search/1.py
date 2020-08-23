# 모의고사

def solution(answers):
    answer = []

    omr = [     # 세 학생들의 찍기 패턴
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    omr_idx = [0,0,0]   # 세 학생들의 찍기 패턴 위치
    omr_length = [5,8,10]   # 세 학생들의 찍기 패턴 길이

    omr_count = [0,0,0]     # 세 학생들의 정답 수

    for number in answers:  # 모든 답안지 순회
        for idx in range(3):    # 세 학생들 모두 체크
            if omr[idx][omr_idx[idx]] == number:    # 학생이 찍은 것 = 정답이면 +1
                omr_count[idx] += 1
            omr_idx[idx] = (omr_idx[idx] + 1) % omr_length[idx] # 학생의 찍기 패턴 위치 이동

    max_count = max(omr_count)  # 최대 정답 수 저장
    for i in range(3):      # 최대 정답자들 저장
        if max_count == omr_count[i]:
            answer.append(i+1)

    return answer
