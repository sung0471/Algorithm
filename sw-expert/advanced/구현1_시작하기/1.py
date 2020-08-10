T = int(input())

for test_case in range(1, T+1):
    length, hex_num = input().split()
    length = int(length)

    result = ''
    for i in range(length):
        num = int(hex_num[i]) if '0' <= hex_num[i] <= '9' else ord(hex_num[i]) - ord('A') + 10
        num = bin(num)[2:]
        result += '0' * (4 - len(num)) + num

    print(f'#{test_case} {result}')
