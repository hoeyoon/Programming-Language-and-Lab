"""
##문제 설명
정수 2개를 입력 받아서 두 수의 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 구하는 프로그램을 작성해보자.

##입력 예시
First Number : 10
Second Number : 4

##출력 예시
Add : 14
Sub : 6
Mul : 40
Div : 2.5
Quo : 2
Rem : 2
"""

a = int(input("First Number : "))
b = int(input("Second Number : "))
print("Add : ",(a + b))
print("Sub : ",(a - b))
print("Mul : ",(a * b))
print("Div : ",(a / b))
print("Quo : ",(a // b))
print("Rem : ",(a % b))
