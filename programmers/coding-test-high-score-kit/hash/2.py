# 해시/전화번호 목록

def solution(phone_book):
    phone_book.sort()   # phone_book list를 정렬
    length = len(phone_book)    # phone 번호의 개수 저장
    for i in range(length - 1):     # 이중 포문으로 모든 index 검색
        for j in range(i+1, length):
            left, right = phone_book[i], phone_book[j]
            if len(left) <= len(right) and left == right[:len(left)]:   # 왼쪽 길이 <= 오른쪽 길이 and 짧은 단어 = 긴 단어의 prefix
                print(left, right)
                return False
    return True

# def solution(phone_book):
#     d = {}
#     for x in phone_book:
#         for i in range(1, len(x) + 1):
#             if x[:i] in d:
#                 d[x[:i]] += 1
#             else:
#                 d[x[:i]] = 1
#
#     for x in phone_book:
#         for i in range(1, len(x) + 1):
#             d[x[:i]] -= 1
#             if d[x[:i]] == 0:
#                 del d[x[:i]]
#         if x in d:
#             return False
#
#         for i in range(1, len(x) + 1):
#             if x[:i] in d:
#                 d[x[:i]] += 1
#             else:
#                 d[x[:i]] = 1
#
#     return True

# def solution(phone_book):
#     answer = True
#     diction =dict()
#     for number in phone_book:
#         diction[number]=1
#
#     for number in phone_book:
#         for i in range(1,len(number)):
#             if number[:i] in diction.keys():
#                 return False
#
#     return answer

# 모든 string을 tree로 되서 개꿀?
