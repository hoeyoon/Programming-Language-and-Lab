"""
## 문제 예시
2차 방정식의 해를 구하는 프로그램을 작성해보자. a, b, c의 값을 입력 받아서, 근의 공식을 사용하여 해를 구한다.
2차 방정식 : y = a * (x ** 2) + b * x + c
근의 공식 : x = (-b +- √(b ** 2 - 4 * a * c)) / 2 * a

## 입력 예시
Number a : 1
Number b : 1
Number c : -6

## 출력 예시
Solution : 2.0, -3.0
"""

a = int(input("Number a : "))
b = int(input("Number b : "))
c = int(input("Number c : "))
s1 = ((-b + ((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
s2 = ((-b - ((b ** 2) - 4 * a * c) ** 0.5)) / 2 * a
print("Solution : %.1f, %.1f" % (s1, s2))
