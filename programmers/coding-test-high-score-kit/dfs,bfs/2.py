# 네트워크

def dfs(curr, n, computers, visit):
    visit[curr] = True
    for i in range(n):
        if curr != n and computers[curr][i] == 1 and not visit[i]:
            dfs(i, n, computers, visit)


def solution(n, computers):
    answer = 0
    visit = [False for _ in range(n)]

    for i in range(n):
        if not visit[i]:
            dfs(i, n, computers, visit)
            answer += 1

    return answer