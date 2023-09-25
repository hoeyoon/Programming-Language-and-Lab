"""
## 문제 설명
정수 하나를 입력 받아서 양수, 0, 음수를 판별하는 프로그램을 작성해보자.

## 입력 예시 1
5

## 출력 예시 1
Positive

## 입력 예시 2
0

## 출력 예시 2
0

## 입력 예시 3
-3

## 출력 예시 3
Negative
"""

a = int(input())
if a > 0:
  print("Positive")
elif a < 0:
  print("Negative")
else:
  print("0")
