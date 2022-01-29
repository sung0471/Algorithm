# 2. 조합적 문제
# 2.2 순열
# 파이썬의 라이브러리를 활용한 순열
import itertools
mylist = [1,2,3]
result = itertools.permutations(mylist)
# result = itertools.permutations(mylist, 3)와 동일

# 파이썬의 라이브러리를 활용한 순열
import itertools
mylist = [1,2,3]
result = itertools.product(mylist, repeat=3)
print(list(result))

# 2.3 부분집합
# 바이너리 카운팅
print('바이너리 카운팅')
arr = [2,3,4,5]
n = len(arr)  # n: 원소의 개수

for i in range(1 << n):  # 1 << n: 부분집합의 개수
    for j in range(n):  # 원소의 수만큼 비트를 비교
        if i & (1 << j):  # i의 j번째 비트가 1이면, j번쨰 원소출력
            print(arr[j], end=',')
    print()

# 2.4 조합
# 재귀적 정의의 표현
# nCr = n-1Cr-1 + n-1Cr
def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r - 1] = an[n - 1]
        comb(n-1, r-1)
        comb(n-1, r)
an = [2,3,4,5]  # n개의 원소를 갖는 리스트
n, r = len(an), 2
tr = [0 for _ in range(r)]  # 조합이 임시 저장될 r개의 크기의 리스트
comb(n, r)

# 파이썬 라이브러리 이용한 조합
import itertools
mylist = [1,2,3]
result = itertools.combinations(mylist, r=2)
print(list(result))
# 파이썬 라이브러리 이용한 중복조합
import itertools
mylist = [1,2,3]
result = itertools.combinations_with_replacement(mylist, 2)
print(list(result))
