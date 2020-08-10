T = int(input())

for test_case in range(1, T+1):
    divisor = 1/2
    num = float(input())
    result = ''
    count = 0

    while num != 0:
        result += str(int(num // divisor))
        num %= divisor
        divisor /= 2
        count += 1

        if count >= 13:
            result = 'overflow'
            break

    print(f'#{test_case} {result}')
