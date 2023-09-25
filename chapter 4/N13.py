"""
## 문제 설명
피보나치 수열을 구하는 프로그램을 작성해보자.
f(x) = f(x - 2) + f(x - 1), f(0) = 1, f(1) = 1 where x >= 0
함수와 배열을 활용하지 않고, 오로지 for문만 활용한다.

## 입력 예시 1
3

## 출력 예시 1
3

## 입력 예시 2
6

## 출력 예시 2
13
"""

n = int(input())
a, b, r = 1, 1, 1
for i in range(2, n + 1):
  r = a + b
  a, b = b, r
print(r)
