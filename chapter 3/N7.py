"""
## 문제 설명
복소수(complex)를 입력 받아서 입력 받은 수의 거리(r)를 계산
하는 프로그램을 작성해보자.
z = x + y*j 일 경우, r = √(x ** 2 + y ** 2)

## 입력 예시
Complex number : 3 + 4j

## 출력 예시
Distance : 5.0
"""

com = complex(input("Complex number : "))
d = (((com.real ** 2) + (com.imag ** 2)) ** 0.5)
print("Distance : %.2f" % d)
