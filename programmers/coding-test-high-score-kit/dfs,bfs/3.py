# 단어 변환

def check_if_change(word, candidate):
    count = 0
    for i in range(len(word)):
        if word[i] != candidate[i]:
            count += 1
        if count > 1:
            return False
    return True


def solution(begin, target, words):
    answer = 0
    queue = [begin]
    visit = [0 for _ in range(len(words))]

    while queue:
        next_queue = []
        for word in queue:
            for i, candidate in enumerate(words):
                if check_if_change(word, candidate) and visit[i] != 2:
                    next_queue.append(candidate)
                    visit[i] = 1
        for i in range(len(visit)):
            if visit[i] == 1:
                visit[i] += 1
        answer += 1

        queue = next_queue[:]
        if target in queue:
            break

    if target not in queue:
        answer = 0

    return answer