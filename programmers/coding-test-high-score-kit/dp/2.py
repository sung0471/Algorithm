# 정수 삼각형

def solution(triangle):
    cumulative = []     # 누적합을 저장하는 배열
    for row in triangle:    # 삼각형의 각 행을 받음
        if len(row) == 1:   # 첫 줄인 경우 cumulative에 깊은복사
            cumulative = row[:]
        else:
            new_line = [0] * len(row)   # 임시로 누적합을 저장할 배열
            for i in range(len(row) - 1):
                # 현재 층의 i 값 = 윗층의 i-1 + 현재 층의 i 중 큰 값
                # 현재 층의 i 값 vs 윗층의 i값 + 현재 층의 i 중 큰 값
                new_line[i] = max(new_line[i], cumulative[i] + row[i])
                # 현재 층의 i+1 값 = 윗층의 i값 + 현재 층의 i+1 값
                new_line[i+1] = cumulative[i] + row[i+1]
            cumulative = new_line[:]    # 계산된 누적합 깊은 복사
    answer = max(cumulative)
    return answer
