"""
## 문제 설명
정수 하나를 입력 받아서 홀수/짝수 여부와 3의 배수 인지를 출력하는 프로그램을 작성해보자.

## 입력 예시 1
3

## 출력 예시 1
Odd and Triple

## 입력 예시 2
2

## 출력 예시 2
Even and Not Triple

## 입력 예시 3
12

## 출력 예시 3
Even and Triple
"""

a = int(input())
if a % 2 == 0:
  print("Even", end=" ")
else:
  print("Odd", end=" ")
if a % 3 == 0:
  print("and Triple")
else:
  print("and Not Triple")
