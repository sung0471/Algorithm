# 여행경로

from copy import deepcopy


def dfs(path, directions, move_count, max_move):
    answer = list()
    candidate = list()
    curr = path[-1]
    # print('start : {}, move_count : {}'.format(curr, move_count))
    queue = []
    direction_list = directions[curr] if curr in directions else {}
    for target, visit in direction_list.items():
        if not visit:
            queue.append(str(target))

    if queue:
        for target in queue:
            target = str(target)
            new_directions = deepcopy(directions)
            new_directions[curr][target] = True
            new_path = [target]
            next_path = dfs(new_path, new_directions, move_count + 1, max_move)
            if isinstance(next_path, list):
                new_path.extend(next_path)
                candidate.append(new_path)

        # print('candidate : ', candidate)
        if len(candidate) == 1:
            answer = candidate[-1]
        elif len(candidate) == 0:
            answer = False
        else:
            target_list = directions[curr].keys()
            next_city = sorted(target_list)[0]
            for path_list in candidate:
                if path_list[0] == next_city:
                    answer += path_list
                    break
    else:
        if move_count == max_move:
            answer = []
        else:
            answer = False

    # print('start({})_result : {}, move_count : {}'.format(path[0], answer, move_count))
    return answer


def solution(tickets):
    directions = dict()
    for ticket in tickets:
        start, end = ticket
        if start not in directions:
            directions[start] = {end: False}
        else:
            directions[start][end] = False

    max_move = len(tickets)
    path = ["ICN"]
    result = dfs(path, directions, 0, max_move)
    result = path + result if isinstance(result, list) else path
    # print(result)
    return result
