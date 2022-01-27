def mergesort(n, arr):
    left_arr, right_arr = arr[0:n // 2], arr[n // 2:n]

    count = 0
    # count = 1 if left_arr[-1] > right_arr[-1] else 0
    # print(left_arr, right_arr)

    if len(left_arr) > 1:
        check_t, left_arr = mergesort(len(left_arr), left_arr)
        count += check_t
    if len(right_arr) > 1:
        check_t, right_arr = mergesort(len(right_arr), right_arr)
        count += check_t

    left_i, right_i = 0, 0
    count += 1 if left_arr[-1] > right_arr[-1] else 0

    merged_arr = []
    while left_i < len(left_arr) and right_i < len(right_arr):
        if left_arr[left_i] < right_arr[right_i]:
            num = left_arr[left_i]
            left_i += 1
        else:
            num = right_arr[right_i]
            right_i += 1

        merged_arr.append(num)

    if left_i < len(left_arr):
        merged_arr.extend(left_arr[left_i:])
    else:
        merged_arr.extend(right_arr[right_i:])

    return count, merged_arr


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    array = list(map(int, input().split()))

    # print(array)
    check_t, result = mergesort(length, array)

    # print(result)
    print('#{} {} {}'.format(test_case, result[length//2], check_t))
