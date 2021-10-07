'''
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
'''
x_l = []
y_l = []
for _ in range(3):
    x, y = map(int, input().split())
    if x not in x_l:
        x_l.append(x)
    else:
        x_l.remove(x)

    if y not in y_l:
        y_l.append(y)
    else:
        y_l.remove(y)

print(x_l[0], y_l[0])
