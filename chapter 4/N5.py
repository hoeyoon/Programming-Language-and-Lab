"""
## 문제 설명
삼각형의 세 변의 길이를 입력 받아서 유효한 삼각형인지 검사하는 프로그램을 작성해보자.
두 변의 합이 세 번째 변보다 커야 한다.

## 입력 예시 1
30 20 40

## 출력 예시 1
Triangle O

## 입력 예시 2
30 20 80

## 출력 예시 2
Triangle X
"""

a, b, c = map(int, input().split())
sum = 0
if a + b > c:
  sum += 1
if a + c > b:
  sum += 1
if b + c > a:
  sum += 1
if sum == 3:
  print("Triangle O")
else:
  print("Triangle X")
