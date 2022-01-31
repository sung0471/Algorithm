def get_pivot(arr):
    n = len(arr)
    # return n//2 index
    return n // 2


def quick_sort(arr):
    pivot_i = get_pivot(arr)
    left_arr, right_arr = list(), list()
    for i, num in enumerate(arr):
        if i == pivot_i:
            pass
        elif arr[i] < arr[pivot_i]:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])

    if len(left_arr) > 1:
        left_arr = quick_sort(left_arr)
    if len(right_arr) > 1:
        right_arr = quick_sort(right_arr)

    new_list = list() + left_arr + [arr[pivot_i]] + right_arr

    return new_list


T = int(input())
for test_case in range(1, 1+T):
    n = int(input())
    A = list(map(int, input().split()))
    result = quick_sort(A)
    print('#{} {}'.format(test_case, result[n//2]))
