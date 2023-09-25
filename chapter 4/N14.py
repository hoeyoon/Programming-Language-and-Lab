"""
## 문제 설명
정수 하나(n)를 입력 받아서 1부터 n까지 숫자 중에서 3의 배수의 숫자들의 합을 구하는 프로그램을 작성해보자.

## 입력 예시 1
3

## 출력 예시 1
3

## 입력 예시 2
6

## 출력 예시 2
9

## 입력 예시 3
9

## 출력 예시 3
18
"""

n = int(input())
sum = 0
for i in range(1, n + 1):
  if i % 3 == 0:
    sum += i
print(sum)
