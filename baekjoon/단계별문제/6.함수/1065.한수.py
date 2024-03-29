'''
문제
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

출력
첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
'''
def check_hansu(n: int) -> bool:
    num = list()
    while n != 0:
        num.append(n%10)
        n //= 10

    gap = num[1] - num[0]
    for i in range(1, len(num) - 1):
        if num[i+1] - num[i] == gap:
            pass
        else:
            return False
    return True

num = int(input())
count = num if num < 100 else 99
for i in range(100, num+1):
    if check_hansu(i):
        count += 1
print(count)