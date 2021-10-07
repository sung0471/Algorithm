'''
문제
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

출력
N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''
def check_prime(n):
    check_p = 0
    for j in range(2, int(n**(1/2))+1):
        if n % j == 0:
            check_p = 1
            break
    if check_p > 0 or n == 1:
        return False
    return True


n = int(input())
if n != 1:
    while n != 1:
        for i in range(2, n+1):
            if n % i == 0 and check_prime(i):
                n //= i
                print(i)
                break

'''
n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        n //= i
        print(i)
    else:
        i += 1
'''