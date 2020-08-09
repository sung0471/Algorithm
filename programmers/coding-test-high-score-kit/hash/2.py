### 해시/전화번호 목록

def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)
    for i in range(length - 1):
        for j in range(i+1, length):
            left, right = phone_book[i], phone_book[j]
            if len(left) <= len(right) and left == right[:len(left)]:
                print(left, right)
                return False
    return True
