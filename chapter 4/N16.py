"""
## 문제 설명
정수 하나(n)를 입력 받아서 소수(prime)인지 판별하는 프로그램을 작성해보자.

## 입력 예시 1
3

## 출력 예시 1
Prime

## 입력 예시 2
7

## 출력 예시 2
Prime

## 입력 예시 3
12

## 출력 예시 3
Not Prime
"""

n = int(input())
count = 0
for i in range(1, n + 1):
  if n % i == 0:
    count += 1
if count == 2:
  print("Prime")
else:
  print("Not Prime")
