# 카펫

def solution(brown, yellow):
    import math
    answer = []

    # brown : 2x + 2y - 4
    # yellow : (x - 2)(y - 2)
    area = brown + yellow   # 면적 구함
    # 세로길이 = 3 ~ sqrt(area)까지 반복
    for col in range(3, int(math.sqrt(area))+1):
        row = area//col     # 가로길이
        # 가로 * 세로 = 면적이면서, brown 수식이 성립하면 종료
        if area % col == 0 and 2 * row + 2 * col - 4 == brown:
            answer = [row, col]
            break
    
    # 한 번 구하면 종료하는 이유 : 가로 >= 세로
    return answer

# import math
# def solution(brown, yellow):
#             w+h                   (w+h)**2     -       4wh
#                                           = (w-h)**2
#     w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
#     return [w,h]
