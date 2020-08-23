# 등굣길

def solution(m, n, puddles):
    area = [[0 for _ in range(n)] for _ in range(m)]    # 길을 표현한 배열
    dp = [[0 for _ in range(n)] for _ in range(m)]  # 최단경로 개수 저장한 배열
    for x, y in puddles:    # 우물인 위치 체크
        area[x-1][y-1] = -1

    for i in range(m):
        for j in range(n):
            if area[i][j] == -1:    # 물 웅덩이는 경로 개수=0
                dp[i][j] = 0
            else:
                if i == 0 and j == 0:   # 시작 위치 = 1
                    dp[i][j] = 1
                elif i == 0 and j > 0:  # [0, j] = 1
                    dp[i][j] = dp[i][j-1]
                elif i > 0 and j == 0:  # [i, 0] = 1
                    dp[i][j] = dp[i-1][j]
                else:   # 왼쪽, 위쪽에서 온 경로 수를 합침
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[m-1][n-1] % 1000000007


# 문제 잘못읽음 -> 최단경로의 크기를 구하는 것으로 착각
a = solution(4,3,[[2, 2]])
print(a)

